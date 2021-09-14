def add_time(start,to_add):
    """
    HH:MM:SS 형식에 HH:MM:SS 형식의 시간을 더하는 함수
    """
    a,b,c = map(int, start.split(':'))
    x,y,z = map(int, to_add.split(':'))
    hour,minute,second = 0,0,0
    if c+z >= 60:
        minute += 1
        second = c+z-60
    else:
        second = c+z
    if minute+b+y >= 60:
        hour += 1
        minute = minute+b+y-60
    else:
        minute += b+y
    hour += a+x
    return str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)

def subtract_time(start,end):
    """
    HH:MM:SS 형식에 HH:MM:SS 형식의 시간을 빼는 함수
    """
    a,b,c = map(int, start.split(':'))
    x,y,z = map(int, end.split(':'))
    hour,minute,second = 0,0,0
    if z-c < 0:
        second = z-c+60
        minute -= 1
    else:
        second = z-c
    if minute+y-b < 0:
        minute = minute+y-b+60
        hour -= 1
    else:
        minute += y-b
    hour += x-a
    return str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)

def convert2second(time):
    """
    HH:MM:SS 형식의 시간을 초 단위로 변환하는 함수
    """
    hour,minute,second = map(int,time.split(':'))
    return hour*3600 + minute*60 + second

def convert2time(second):
    """
    초 단위 시간을 HH:MM:SS 형식으로 바꾸는 함수
    """
    hour = second // 3600
    if hour >= 1:
        second -= hour * 3600
    minute = second // 60
    if minute >= 1:
        second -= minute * 60
    return str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)