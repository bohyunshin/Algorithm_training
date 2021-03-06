n,m = map(int,input().split())
money = []
for _ in range(n):
    money.append(int(input()))
d = [10001]*(m+1)
d[0] = 0
for i in range(1,m+1):
    for k in money:
        if i-k >= 0:
            if d[i] == 0 or d[i] > d[i-k]+1:
                d[i] = d[i-k]+1
print(d[m])