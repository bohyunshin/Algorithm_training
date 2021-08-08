import sys
sys.setrecursionlimit(1000000)

n = int(input())
A = []
for _ in range(n):
    A.append(input())
color = [[-1]*n for _ in range(n)]
dx = [-1,1,0,0,-1,1]
dy = [0,0,-1,1,1,-1]
ans = 0

# 만약 색칠해야하는 node가 이분 그래프라면, 두 개의 색으로 모두 칠할 수 있음.
# 이분 그래프가 아니라면 최대로 칠할 수 있는 색깔의 수는 3개임.
# 만약에 색칠해야하는 부분이 하나도 없으면 색깔의 수는 0개.

# x,y: 방문 노드, c: 칠해야하는 색.
def dfs(x, y, c):
    global ans
    color[x][y] = c
    # 색칠해야하는 부분이 하나라도 있으면 색깔의 수는 1개.
    # dfs 함수 호출된 것 자체가 A[i][j] == 'X'라는 뜻임.
    ans = max(ans, 1)
    # 인접 노드 살펴봄.
    for k in range(6):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if A[nx][ny] == 'X':
                if color[nx][ny] == -1:
                    # 이분 그래프에서 색 칠하듯이 두 가지 색으로 칠해봄.
                    dfs(nx, ny, 1-c)
                # 우선 이분 그래프라고 생각하고 답을 2로 해주고,
                ans = max(ans, 2)
                # 만약 인접한 곳의 색깔이 현재 위치의 색과 똑같이 칠해졌다면,
                # 이분 그래프가 아닌 것임. 따라서 정답은 최대값 3으로 해줌.
                if color[nx][ny] == c:
                    ans = max(ans, 3)


for i in range(n):
    for j in range(n):
        if A[i][j] == 'X' and color[i][j] == -1:
            dfs(i, j, 0)

print(ans)