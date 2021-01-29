n,m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

d = [10001]*(m+1)
d[0] = 0

for i in range(1, m+1):
    for j in range(len(money)):
        if i-money[j] >= 0:
            d[i] = min(d[i], d[i-money[j]] + 1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])