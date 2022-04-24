n = int(input())
a = []
for _ in range(n):
    x,y = map(int,input().split())
    a.append((x,y))
a.sort(key=lambda x: x[0])
l = []
for i in range(n):
    l.append(a[i][1])
dp = [1]*n
for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))