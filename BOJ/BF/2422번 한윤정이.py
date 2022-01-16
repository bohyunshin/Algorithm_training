from collections import defaultdict
n,m = map(int,input().split())
options = defaultdict(bool)
for _ in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    tmp = sorted([x,y])
    options[tuple(tmp)] = True
a = [-1]*3
c = [False]*n
ans = 0
def go(index,i):
    global ans
    if index == 3:
        ans += 1
        return
    if i >= n:
        return
    FLAG = False
    ices = [j for j in a if i != -1]
    for ice in ices:
        tmp = tuple(sorted([ice,i]))
        if options[tmp]:
            FLAG = True
            break
    if FLAG == False:
        a[index] = i
        go(index+1,i+1)
    a[index] = -1
    go(index,i+1)
go(0,0)
print(ans)