def check(apeach, lion):
    apeach = apeach[::-1]
    lion = lion[::-1]
    apeach_score = 0
    lion_score = 0
    for score, (a, l) in enumerate(zip(apeach, lion)):
        if a == l and l != 0:
            apeach_score += score
        elif a > l:
            apeach_score += score
        elif a < l:
            lion_score += score
    return apeach_score, lion_score


def recursive(index, m, lst):
    global a, c, order, cases
    if index >= m:
        cases.append(a[:])
        return
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i != index:
                continue
            if c[i][j] or order[i]:
                continue
            c[i][j] = True
            order[i] = True
            a[index] = lst[i][j]
            recursive(index + 1, m, lst)
            c[i][j] = False
            order[i] = False


def solution(n, info):
    global a, c, order, cases
    step = []
    for i in info:
        if i == n:
            step.append([0])
        else:
            step.append([0, i + 1])

    a = [0] * 11
    order = [False] * 11
    c = [[] for _ in range(11)]
    for i in range(len(step)):
        for _ in range(len(step[i])):
            c[i].append(False)
    cases = []
    recursive(0, n, info)
    for i in cases:
        print(i)
info = [2,1,1,1,0,0,0,0,0,0,0]
result = [0,2,2,0,1,0,0,0,0,0,0]
n = 5
solution(n,info)