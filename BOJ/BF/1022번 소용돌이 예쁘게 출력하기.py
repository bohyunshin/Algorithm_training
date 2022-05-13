r1,c1,r2,c2 = map(int,input().split())
if r1 == c1 == r2 == c2 == 0:
    print(1)
    exit()
n = max(abs(r1),abs(c1),abs(r2),abs(c2))
n = n*2 + 1
x,y = n//2, n//2
l = 1
m = n // 2
r1 += m
c1 += m
r2 += m
c2 += m
a = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
d = 0
v = 1
cnt = 0
flag = False
while True:
    for _ in range(4):
        for i in range(l):
            if v == n*n + 1:
                flag = True
                break
            if r1 <= x <= r2 and c1 <= y <= c2:
                a[x-r1][y-c1] = v
            if i != l-1:
                x += dx[d]
                y += dy[d]
                v += 1
        if flag:
            break
        d = (d+1)%4
        if d == 0 and v != 0:
            pass
        else:
            x += dx[d]
            y += dy[d]
        v += 1
    if x == 0 and y == 0:
        break
    y -= 1
    l += 2
    if flag:
        break
val = -1
for i in a:
    val = max(val, max(i))
l = len(str(val))
for i in a:
    tmp = [' '*(l-len(str(k))) + str(k) for k in i]
    print(' '.join(map(str,tmp)))