def solution(s):
    mid = len(s) // 2

    len_list = []

    for step in range(1, mid + 1):
        result = ''
        previous = ''
        count = 1
        for j in range(0, len(s), step):
            current = s[j:j + step]
            if previous == current:
                count += 1
            else:
                result += (previous if count == 1 else str(count) + previous)
                count = 1
            previous = current
        # 나머지 처리
        # current = s[j:]
        # if previous == current:
        #         count += 1
        # else:
        #     count = 1
        # result += (previous if count == 1 else str(count)+previous)
        result += (previous if count == 1 else str(count) + previous)
        len_list.append(len(result))
    return min(len_list)