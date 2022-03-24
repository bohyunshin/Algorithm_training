import sys
input = sys.stdin.readline
t = int(input())
d = [(1,1), (1,-1), (-1,1), (-1,-1)]
while True:
    try:
        n = int(input())
    except:
        exit()
    l = 10
    coords = {}
    ans = 1
    for _ in range(n):
        x,y = map(int,input().split())
        # x = 10000-x
        coords[(x,y)] = 1
    for x,y in coords.keys():
        for i in range(4):
            tmp = 0
            dx,dy = d[i]
            for j in range(l+1):
                nx = x + j*dx
                for k in range(l+1):
                    ny = y + k*dy
                    if 0 <= nx < 10000 and 0 <= ny < 10000 and coords.get((nx,ny)) != None:
                        tmp += 1
            ans = max(ans,tmp)
    print(ans)