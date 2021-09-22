from collections import deque
A = []
for _ in range(3):
    A.append(list(map(int,input().split())))
def make_key(A):
    result = []
    for i in range(3):
        result.append(' '.join(list(map(str,A[i]))))
    return '\n'.join(result)
def make_mat(A_str):
    tmp = A_str.split('\n')
    result = []
    for i in range(3):
        result.append(list(map(int,tmp[i].split())))
    return result
target_mat = [[1,2,3],[4,5,6],[7,8,0]]
target_key = make_key(target_mat)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = {}
key = make_key(A)
visited[key] = 0
q = deque()
q.append(key)
while q:
    A_str = q.popleft()
    if A_str == target_key:
        print(visited[A_str])
        exit()
    A = make_mat(A_str)
    for x in range(3):
        for y in range(3):
            if A[x][y] == 0:
                blank = x,y
                break
    for i in range(4):
        x,y = blank
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            change_val = A[nx][ny]
            A[x][y] = change_val
            A[nx][ny] = 0
            key = make_key(A)
            if key not in visited.keys():
                q.append(key)
                visited[key] = visited[A_str] + 1
            # 다시 원래대로 되돌려 놓음.
            A[nx][ny] = change_val
            A[x][y] = 0
print(-1)