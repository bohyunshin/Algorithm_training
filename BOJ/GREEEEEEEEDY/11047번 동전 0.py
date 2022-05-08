n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
ans = 0
for coin in coins[::-1]:
    if coin > k:
        continue
    div,mod = k // coin, k % coin
    ans += div
    k = mod
print(ans)