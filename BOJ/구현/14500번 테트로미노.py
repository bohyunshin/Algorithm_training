from copy import deepcopy
def move_to_zero(blocks):
    MIN_x = 1e100
    MIN_y = 1e100
    result = []
    for x,y in blocks:
        if MIN_x > x:
            MIN_x = x
        if MIN_y > y:
            MIN_y = y
    for x,y in blocks:
        x -= MIN_x
        y -= MIN_y
        result.append((x,y))
    return result

def rotate(blocks,n):
    result = []
    for x,y in blocks:
        result.append((y,n-x-1))
    return move_to_zero(result)

def turn_upper(blocks):
    MIN_x = 1e100
    for x,y in blocks:
        if MIN_x > x:
            MIN_x = x
    result = []
    for x,y in blocks:
        nx = MIN_x - (x-MIN_x+1)
        result.append((nx,y))
    return move_to_zero(result)

def turn_left(blocks):
    MIN_y = 1e100
    for x,y in blocks:
        if MIN_y > y:
            MIN_y = y
    result = []
    for x,y in blocks:
        ny = MIN_y - (y-MIN_y+1)
        result.append((x,ny))
    return move_to_zero(result)

def check(blocks,n,m):
    for x,y in blocks:
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
    return True

# 후보 블록 무식하게 쓰기.
# blocks = [
#     [(0,0),(0,1),(0,2),(0,3)],
#     [(0,0),(1,0),(2,0),(3,0)],
#
#     [(0,0),(0,1),(1,0),(1,1)],
#
#     [(0,0),(1,0),(2,0),(2,1)],
#     [(0,0),(0,1),(0,2),(1,0)],
#     [(0,0),(0,1),(1,1),(2,1)],
#     [(1,0),(1,1),(1,2),(0,2)],
#     [(2,0),(2,1),(1,1),(0,1)],
#     [(0,0),(1,0),(1,1),(1,2)],
#     [(0,0),(0,1),(1,0),(2,0)],
#     [(0,0),(0,1),(0,2),(1,2)],
#
#     [(0,0),(1,0),(1,1),(2,1)],
#     [(1,0),(1,1),(0,1),(0,2)],
#     [(2,0),(1,0),(1,1),(0,1)],
#     [(0,0),(0,1),(1,1),(1,2)],
#
#     [(0,0),(0,1),(0,2),(1,1)],
#     [(1,0),(0,1),(1,1),(2,1)],
#     [(1,0),(1,1),(1,2),(0,1)],
#     [(0,0),(1,0),(2,0),(1,1)],
# ]

n,m = map(int,input().split())
N = max(n,m)
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
ans = -1

# 후보 블록 미리 추리기.
blocks = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(0,1),(1,0),(1,1)],
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,0),(1,0),(1,1),(2,1)],
    [(0,0),(0,1),(0,2),(1,1)]
]
candidates = []
for block in blocks:
    block_left = turn_left(block)
    block_upper = turn_upper(block)
    block_left.sort()
    block_upper.sort()

    for _ in range(4):
        block_left = rotate(block_left,N)
        if block_left not in candidates:
            candidates.append(block_left)
    for _ in range(4):
        block_upper = rotate(block_upper,N)
        if block_upper not in candidates:
            candidates.append(block_upper)

for block in blocks:
    for _ in range(4):
        block = rotate(block,N)
        block.sort()
        if block not in candidates:
            candidates.append(block)

for block in candidates:

    for i in range(n):
        for j in range(m):
            block_move = []
            for x,y in block:
                block_move.append((x+i,y+j))
            if check(block_move,n,m):
                tmp = 0
                for x,y in block_move:
                    tmp += A[x][y]
                ans = max(ans,tmp)
print(ans)


"""
4 5
1 1 1 1 0
1000 1 100 100 0
1 1000 1000 100 101
0 0 100 101 0

4 5
1 1 1 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""