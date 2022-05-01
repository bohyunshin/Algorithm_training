n = int(input())
a = [0] + list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
dp = [[0]*(n*500+1) for _ in range(n+1)]
def go(idx,weight):
    if idx > n:
        return
    print(idx, weight, dp[idx][weight])
    if dp[idx][weight]:
        return

    dp[idx][weight] = 1
    go(idx+1,weight)
    go(idx+1,weight + a[idx+1])
    go(idx+1,abs(weight - a[idx+1]))
go(0,0)
for k in b:
    flag = False
    if k > 500*n:
        print('N', end=' ')
    for i in range(n):
        if dp[i][k]:
            flag = True
            break
    if flag:
        print('Y', end=' ')
    else:
        print('N', end=' ')
for i in dp:
    print(i)