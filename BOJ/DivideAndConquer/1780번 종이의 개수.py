n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
def check(x1,y1,x2,y2):
    tmp = set()
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            tmp.add(a[i][j])
    if len(tmp) == 1:
        return list(tmp)[0]
    else:
        return -100
# -1, 0, 1
x,y,z = 0,0,0
def go(x1,y1,x2,y2):
    global x,y,z
    if x1 == x2 and y1 == y2:
        if a[x1][y1] == -1:
            x += 1
        elif a[x2][y2] == 0:
            y += 1
        else:
            z += 1
        return
    else:
        v = check(x1,y1,x2,y2)
        if v != -100:
            if v == -1:
                x += 1
            elif v == 0:
                y += 1
            else:
                z += 1
            return
    l = x2-x1+1
    step = l // 3
    r = [x1+step*i for i in range(3)]
    c = [y1+step*i for i in range(3)]
    for i in r:
        for j in c:
            x1,y1 = i,j
            x2,y2 = i+step-1, j+step-1
            go(x1,y1,x2,y2)
go(0,0,n-1,n-1)
print(x)
print(y)
print(z)