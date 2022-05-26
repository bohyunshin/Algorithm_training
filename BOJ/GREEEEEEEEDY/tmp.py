import json
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

from tools.kafka_producer import KafkaProducer


class KafkaLoggingHandler(RotatingFileHandler):
    def __init__(
        self,
        topic,
        config,
        log_format,
        additional_fields,
        max_buffer_size,
        kafka_log_level=logging.WARNING,
        file_log_name=None,
        file_log_level=logging.INFO,
        file_mode="a",
        file_max_bytes=0,
        file_backup_count=0,
        file_encoding="utf-8",
        file_delay=0,
        log_type="kafka-log",
    ):
        """Create a new KafkaLoggingHandler object.

                This class implements a new Python logging handler to ship logs to kafka.
                It uses the RotatingFileHandler of Python basically and adds a new handler
                using confluent-kafka to send some logs to kafka.

                If file_log_name is None, KafkaLoggingHandler does not save logs to a file and
                ignores other file_* arguments.

                Parameters
                ----------
                topic : str
                    your kafka topic name created at Verda kafka.
                config : dict
                    your kafka configuration imported from LINE-Shield/shield-conf.
                log_format : str
                    your log format defined for logger.
                additional_fields : dict
                    your additional fields that should be included in kafka message.
                max_buffer_size : int
                    your maximum buffer size which is criteria for sending messages to kafka
                kafka_log_level : ``logging.CRITICAL`` ~ ``logging.NOTSET`` (optional)
                    logging level.
                file_log_name : str (optional)
                file_log_level : ``logging.CRITICAL`` ~ ``logging.NOTSET`` (optional)
                file_mode : str (optional)
                file_max_bytes : int (optional)
                file_backup_count : int (optional)
                file_encoding : str (optional)
                file_delay : int (optional)
                log_type   : str (optional)
                """
        if file_log_name is not None:
            self.write_file_mode = True
            super().__init__(
                file_log_name,
                file_mode,
                file_max_bytes,
                file_backup_count,
                file_encoding,
                file_delay,
            )
        else:
            self.write_file_mode = False
            super(logging.FileHandler, self).__init__()

        self.topic = topic
        self.config = config
        self.setLevel(file_log_level)
        self.setFormatter(logging.Formatter(log_format))
        self.kafka_log_level = kafka_log_level
        self.log_type = log_type

        self.max_buffer_size = max_buffer_size
        self.buffer = []
        self.additional_fields = additional_fields

    def emit(self, record):
        # If current log level is the same or higher than predefined log level,
        # send logs to kafka topic.
        if record.levelno >= self.kafka_log_level:

            self.buffer.append(record)

            # After `service.start` does all of its jobs,
            # python garbage collection algorithm is executed.
            # As a result, __del__ method is run, which is stored
            # as a flag variable in `is_end`
            is_end = record.funcName == "__del__"

            # If the log level is equal to ERROR,
            # flush it with logs from buffer
            is_error = record.levelname == "ERROR"

            if len(self.buffer) >= self.max_buffer_size or is_end or is_error:
                self._flush()

    def _flush(self):
        if self.buffer:
            # get logs from buffer
            logs_from_buffer = self.buffer
            # empty buffer
            self.buffer = []

            kafka = KafkaProducer(topic=self.topic, config=self.config)
            kafka.connect()

            for log in logs_from_buffer:
                # If log level is equal to Error, the error message could be quite long,
                # which could cause http request error in ES open distro.
                # So, send first line in error message
                msg = self.format(log).split("\n")[0] if log.levelname == "ERROR" else self.format(log)
                log_json = {
                    "message": msg,
                    "model_name": self.additional_fields["model_name"],
                    "source": self.additional_fields["source"],
                    "stage": self.additional_fields["stage"],
                    "log_time": self.additional_fields["log_time"],
                    "log_level": log.levelname,
                }
                dump_log = json.dumps(log_json, default=str).encode("utf-8")
                try:
                    ts = int(datetime.timestamp(datetime.now()) * 1000)
                    key = (self.additional_fields["model_name"] + " " + str(ts)).encode(
                        "utf-8"
                    )
                    kafka.produce(data=dump_log, key=key)
                except Exception as e:
                    logging.warning(f"kafka produce occur error {e}")

                # If write_file mode, write logs to a file.
                if self.write_file_mode:
                    super().emit(log)

            kafka.flush()
