from collections import defaultdict
n = int(input())
c = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
like_mapping = defaultdict(list)

def check(like,c):
    loc = []
    zero_loc = []
    for i in range(n):
        for j in range(n):
            if c[i][j] in like:
                loc.append((i,j))
            if c[i][j] == 0:
                zero_loc.append((i,j))
    if len(loc) >= 1:
        return loc
    else:
        return zero_loc

for i in range(n**2):
    tmp = list(map(int,input().split()))
    s,like = tmp[0],tmp[1:]
    like_mapping[s] += like
    # if i == 0:
    #     c[1][1] = s
    #     continue
    like_loc = defaultdict(int)
    like_nearby_blank = defaultdict(int)
    a = check(like,c)
    for x,y in a:
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and c[nx][ny] == 0:
                like_loc[(nx,ny)] += 1
                for p in range(4):
                    nnx,nny = nx+dx[p],ny+dy[p]
                    if 0 <= nnx < n and 0 <= nny < n and c[nnx][nny] == 0:
                        like_nearby_blank[(nx,ny)] += 1
    if len(like_loc.keys()) == 1:
        row,col = list(like_loc.keys())[0]
        c[row][col] = s
    elif len(like_loc.keys()) == 0:
        FLAG = False
        tmp = []
        for x in range(n):
            for y in range(n):
                blank_cnt = 0
                if c[x][y] == 0:
                    for i in range(4):
                        nx,ny = x+dx[i],y+dy[i]
                        if 0 <= nx < n and 0 <= ny < n and c[nx][ny] == 0:
                            blank_cnt += 1
                    tmp.append((x,y,blank_cnt))
        tmp.sort(key=lambda x: (-x[2],x[0],x[1]))
        row,col = tmp[0][0],tmp[0][1]
        c[row][col] = s
    else:
        tmp = []
        for x,y in like_loc.keys():
            tmp.append((x,y,like_loc[(x,y)],like_nearby_blank[(x,y)]))
        tmp.sort(key=lambda x: (-x[2],-x[3],x[0],x[1]))
        row,col = tmp[0][0],tmp[0][1]
        c[row][col] = s

ans = 0
for x in range(n):
    for y in range(n):
        s = c[x][y]
        like = like_mapping[s]
        cnt = 0
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if c[nx][ny] in like:
                    cnt += 1
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)

"""
3
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
6 7 8 9 1
7 8 9 1 2
8 9 1 2 3
9 1 2 3 4
"""