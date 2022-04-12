k = int(input())
y,x = map(int,input().split())
y -= 1
x = 2**k-x
a = [[0]*(2**k) for _ in range(2**k)]
a[x][y] = -1

def check(sz, x, y):
    for i in range(x,x+sz):
        for j in range(y,y+sz):
            if a[i][j] != 0:
                return False
    return True
def sol(sz,x,y):
    global num
    num += 1
    s = sz // 2
    if check(s, x, y):
        a[x+s-1][y+s-1] = num
    if check(s, x, y+s):
        a[x+s-1][y+s] = num
    if check(s, x+s, y):
        a[x+s][y+s-1] = num
    if check(s, x+s, y+s):
        a[x+s][y+s] = num
    if sz == 2:
        return
    sol(s, x, y)
    sol(s, x+s, y)
    sol(s, x, y+s)
    sol(s, x+s, y+s)
num = 0
sol(2**k,0,0)
for i in a:
    print(' '.join(map(str,i)))
