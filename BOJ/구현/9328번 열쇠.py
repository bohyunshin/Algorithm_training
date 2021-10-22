from string import ascii_uppercase,ascii_lowercase
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 처음에 계속 돌면서 가능한 모든 열쇠를 찾아야 함.
def check(A,key):
    for i in range(n):
        for j in range(m):
            if A[i][j] in ascii_uppercase and A[i][j].lower() in key:
                return True
    return False
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A = []
    for _ in range(n):
        A.append([i for i in input()])
    key = input()
    key = '' if key == '0' else key
    ans = 0
    loop = 0
    while True:
        before_key = key
        visited = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # print(i,j,n,m)
                if 1 <= i <= n-2 and 1 <= j <= m-2:
                    continue
                # print(i,j,n,m)
                if A[i][j] == '*':
                    continue
                if A[i][j] == '$':
                    ans += 1
                    A[i][j] = '.'
                if A[i][j] in ascii_uppercase:
                    if A[i][j].lower() in key:
                        A[i][j] = '.'
                    else:
                        continue
                if A[i][j] in ascii_lowercase:
                    key += A[i][j]
                    A[i][j] = '.'
                q = deque()
                q.append((i,j))
                visited[i][j] = True
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and A[nx][ny] != '*':
                            if A[nx][ny] in ascii_uppercase:
                                if A[nx][ny].lower() in key:
                                    A[nx][ny] = '.'
                                else:
                                    continue
                            elif A[nx][ny] in ascii_lowercase:
                                key += A[nx][ny]
                                A[nx][ny] = '.'
                            elif A[nx][ny] == '$':
                                A[nx][ny] = '.'
                                ans += 1
                            # 빈칸인 경우.
                            visited[nx][ny] = True
                            q.append((nx,ny))
        if before_key == key:
            break
    # for i in A:
    #     print(''.join(i))
    # print(key,ans)
    print(ans)