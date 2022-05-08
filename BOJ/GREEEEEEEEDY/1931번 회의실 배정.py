n = int(input())
a = []
for _ in range(n):
    x,y = map(int,input().split())
    a.append((x,y))
a.sort(key=lambda x: (x[1],x[0]))
ans = 1
end = a[0][1]
for i in range(1,n):
    x,y = a[i]
    if x >= end:
        end = y
        ans += 1
print(ans)