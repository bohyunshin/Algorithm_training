n = int(input())
hard = []
weight = []
for _ in range(n):
    x,y = map(int,input().split())
    hard.append(x)
    weight.append(y)
ans = 0
def go(index,hard):
    global ans
    if index == n:
        tmp = 0
        for i in range(n):
            if hard[i] <= 0:
                tmp += 1
        ans = max(ans,tmp)
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
            continue
        hard[index] -= weight[i]
        hard[i] -= weight[index]
        go(index+1,hard.copy())
        hard[index] += weight[i]
        hard[i] += weight[index]
    if cnt == n-1:
        go(index+1,hard.copy())
go(0,hard)
print(ans)