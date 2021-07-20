from collections import deque
k = int(input())
w,h = map(int, input().split())
array = []
for _ in range(h):
    array.append( list(map(int,input().split())) )

dx_horse = [ -1,-2,-2,-1,1,2,2,1 ]
dy_horse = [ -2,-1,1,2,2,1,-1,-2 ]

dx_monkey = [-1,1,0,0]
dy_monkey = [0,0,-1,1]

q = deque()
start = (0,0)
q.append(start)
myhash = {}
horse_nums = {}
for i in range(h):
    for j in range(w):
        myhash[(i,j)] = []
        horse_nums[(i, j)] = []

myhash[start].append( (k,0) )
a = 0
while q:
    a += 1
    x,y = q.popleft()
    if (x == h-1 and y == h-1) or a >= 1e6:
        break
    for k,dist in myhash[(x,y)]:
        if k >= 1:
            for i in range(len(dx_horse)):
                nx = x + dx_horse[i]
                ny = y + dy_horse[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if array[nx][ny] != 1:

                        if len(myhash[(nx,ny)]) == 0:
                            myhash[(nx,ny)].append( (k-1, dist + 1) )
                            q.append((nx,ny))
                        else:
                            # if myhash[(nx, ny)] > myhash[(x, y)] + 1:
                            #     myhash[(nx, ny)] = myhash[(x, y)] + 1
                            #     q.append((nx,ny))
                            #     horse_nums[(nx, ny)] = k - 1
                            if (k - 1, dist + 1) not in myhash[(nx,ny)]:
                                myhash[(nx, ny)].append((k - 1, dist + 1))
                                q.append((nx,ny))
        for i in range(len(dx_monkey)):
            nx = x + dx_monkey[i]
            ny = y + dy_monkey[i]
            if 0 <= nx < h and 0 <= ny < w:
                if array[nx][ny] != 1:
                    if len(myhash[(nx, ny)]) == 0:
                        myhash[(nx, ny)].append((k, dist + 1))
                        q.append((nx, ny))
                    else:
                        # if myhash[(nx, ny)] > myhash[(x, y)] + 1:
                        #     myhash[(nx, ny)] = myhash[(x, y)] + 1
                        #     q.append((nx,ny))
                        #     horse_nums[(nx, ny)] = k - 1
                        if (k, dist + 1) not in myhash[(nx, ny)]:
                            myhash[(nx, ny)].append((k, dist + 1))
                            q.append((nx, ny))

if (h-1,w-1) not in myhash.keys():
    print(-1)
else:
    print(sorted(myhash[(h-1,w-1)], key=lambda x: x[1])[0][1])