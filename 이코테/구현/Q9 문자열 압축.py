def solution(s):
    n = len(s)
    max_split = n // 2
    result = []

    if n == 1:
        return 1

    for step in range(1, max_split + 1):
        comp_s = ''
        count = 1
        previous = s[0:step]
        for j in range(step, n, step):
            if previous == s[j:j + step]:
                count += 1
            else:
                comp_s += str(count) + previous if count != 1 else previous
                count = 1
                previous = s[j:j + step]
        comp_s += str(count) + previous if count != 1 else previous
        result.append(len(comp_s))
    return min(result)


