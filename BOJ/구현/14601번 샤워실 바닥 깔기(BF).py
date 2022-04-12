k = int(input())
y,x = map(int,input().split())
y -= 1
x = 2**k-x
a = [[0]*(2**k) for _ in range(2**k)]
a[x][y] = -1

def get_tile(x,y):
    coords = [(x,y),(x,y+1),(x+1,y),(x+1,y+1)]
    nums = [[0,1,2],[0,1,3],[1,2,3],[0,2,3]]
    tiles = []
    for num in nums:
        tmp = []
        for i in num:
            tmp.append(coords[i])
        tiles.append(tmp)
    return tiles

def check():
    v = 0
    for i in range(2**k):
        for j in range(2**k):
            if a[i][j] == -1:
                continue
            if a[i][j] >= 1:
                v += 1
    return v == (2**k)**2 - 1

def go(block,num):
    if num == (2**k - 1)**2 - 1:
        if check():
            for i in a:
                print(i)
            exit()
            return
    start_i,start_j = num // 3, num % 3
    for i in range(start_i,2**k-1):
        for j in range(start_j,2**k-1):
            # 타일을 놓는 경우.
            tiles = get_tile(i,j)
            for tile in tiles:
                cnt = 0
                for x,y in tile:
                    if a[x][y] == 0:
                        cnt += 1
                if cnt == 3:
                    for x,y in tile:
                        a[x][y] = block
                    go(block+1,num+1)
                    for x,y in tile:
                        a[x][y] = 0
            # 타일 놓지 않는 경우.
            go(block, num + 1)
go(1,0)
