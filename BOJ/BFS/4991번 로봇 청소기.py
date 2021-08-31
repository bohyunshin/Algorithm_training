from collections import deque
from itertools import permutations
def bfs(x1,y1,A):
    n = len(A)
    m = len(A[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    visited[x1][y1] = 0
    q.append((x1,y1))
    while q:
        x,y, = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and \
                A[nx][ny] != 'x' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
    return visited

def solution(n,m,A):
    dirty = []
    for i in range(n):
        for j in range(m):
            if A[i][j] == 'o':
                start = (i,j)
                A[i][j] = '.'
            if A[i][j] == '*':
                dirty.append((i,j))
    # 방법의 결과 수를 담을 리스트.
    ways = []
    # 시작점별로 과거 BFS 이력을 담을 dictionary.
    # 시작점 + 먼지의 포인트만큼 우선 BFS를 해줘서 그 결과를 담아둘 곳임.
    BFS = {}
    BFS[start] = bfs(start[0],start[1],A)
    for i,j in dirty:
        BFS[(i,j)] = bfs(i,j,A)

    for p in permutations(dirty):
        move = 0
        s = BFS[start]
        # 시작점 -> 첫 번째 드러운 지점으로 가는 경우.
        # -1이면 바로 -1 추가해주고 다음 경우 살펴보면 됨.
        if s[p[0][0]][p[0][1]] == -1:
            ways.append(-1)
            continue
        else:
            FLAG = False
            move += s[p[0][0]][p[0][1]]
            A[p[0][0]][p[0][1]] = 'o'
            for i in range(len(p)-1):
                start_point = (p[i][0],p[i][1])
                tmp = BFS[start_point]
                # 중간에 못가는 경로가 있으면 바로 -1 값 추가해주고
                # 그 뒤는 안가봐도 됨. FLAG는 True로 바꿔준다.
                if tmp[p[i+1][0]][p[i+1][1]] == -1:
                    ways.append(-1)
                    FLAG = True
                    break
                else:
                    move += tmp[p[i+1][0]][p[i+1][1]]
            if FLAG == False:
                ways.append(move)
    return ways

if __name__ == '__main__':
    while True:
        m,n = map(int, input().split())
        if m == n == 0:
            break
        A = []
        for _ in range(n):
            A.append([i for i in input()])

        print(min(solution(n,m,A)))