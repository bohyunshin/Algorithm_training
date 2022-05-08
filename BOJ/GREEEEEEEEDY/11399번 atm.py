n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
total = n
for i in range(n):
    ans += a[i]*total
    total -= 1
print(ans)