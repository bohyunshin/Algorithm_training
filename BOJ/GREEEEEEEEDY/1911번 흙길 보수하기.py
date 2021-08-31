n,l = map(int, input().split())
ans = 0
index = 0
last = 0
A = []
for _ in range(n):
    a,b = map(int, input().split())
    A.append((a,b))
A.sort(key=lambda x: x[0])
for x,y in A:
    if last >= x:
        x = last+1
    div,mod = (y-1-(x-1)) // l, (y-1-(x-1)) % l
    if mod == 0:
        ans += div
        last = x + div*l - 1
    else:
        ans += div+1
        last = x + (div+1)*l - 1
print(ans)