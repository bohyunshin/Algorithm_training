from collections import Counter

def solution(N, stages):
    answer = []
    attempt = [0] * (max(stages) + 1)
    for s in stages:
        for i in range(1, s + 1):
            attempt[i] += 1
    c = Counter(stages)
    result = []

    for i in range(1, N + 1):
        try:
            failure = c[i] / attempt[i]
        except:
            failure = 0
        result.append((failure, i))
    result.sort(key=lambda x: (-x[0], x[1]))
    return [i[1] for i in result]