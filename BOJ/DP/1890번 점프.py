from collections import deque

n = int(input())
array = []
for _ in range(n):
    array.append( list(map(int, input().split())) )
d = [[0]*n for _ in range(n)]

start = (0,0)
q = deque()
q.append(start)
result = 0

while q:
    # print(q,result)
    x,y = q.popleft()
    current = d[x][y]
    dist = array[x][y]
    # 오른쪽으로 이동하기
    if y + dist < n:
        if x == n-1 and y+dist == n-1:
            result += 1
            continue
        else:
            d[x][y + dist] = current + 1
            q.append((x,y+dist))
    # 아래로 이동하기
    if x + dist < n:
        if x+dist == n-1 and y == n-1:
            result += 1
            continue
        else:
            d[x + dist][y] = current + 1
            q.append((x+dist,y))
print(result)