n = int(input())
hard = []
weight = []
for _ in range(n):
    x,y = map(int,input().split())
    hard.append(x)
    weight.append(y)
def go(index,hard):
    if index == n:
        print(hard)
        return
    if hard[index] <= 0:
        go(index+1,hard.copy())
        return
    cnt = 0
    for i in range(n):
        if i == index:
            continue
        if hard[i] <= 0:
            cnt += 1
    if cnt == n-1:
        go(index+1,hard.copy())
        return
    for i in range(n):
        if i == index:
            continue
        if hard[i] <= 0:
            cnt += 1
            continue
        hard[index] -= weight[i]
        hard[i] -= weight[index]
        go(index+1,hard.copy())

go(0,hard)