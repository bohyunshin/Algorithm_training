from math import floor

n,l,r = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
# 똑같이 dfs 구현하는데
# 인구이동 조건만 추가해줌
def dfs(x,y,visited,cnt):
    visited[x][y] = True
    ally[x][y] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] is False and l <= abs(A[x][y] - A[nx][ny]) <= r:
                dfs(nx,ny,visited,cnt)

def get_max(lst):
    result = -1e100
    n = len(lst)
    for i in range(n):
        result = max(result, max(lst[i]))
    return result

answer = 0
while True:
    # ally, visited는 인구 이동이 한번 일어나고 다시 초기화해줌.
    # 연합 정보를 담음
    ally = [[0]*n for _ in range(n)]
    # 방문 여부를 담음
    visited = [[False]*n for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # 동맹 알아내기.
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] is False:
                cnt += 1
                # 이거 하니까 시간 초과 떴음
                # 아마도 O(N^4)가 되어서? -> 100^4 = 10^8 = 1억
                # cnt = get_max(ally())
                dfs(i,j,visited,cnt)
    # 인구 이동하기.
    num_ally = cnt
    # 연합의 수가 총 도시의 수와 같다면 모두 각각이 연합인 것임
    # 이때는 인구 이동이 일어나지 않으므로 ㅌㅌ
    if num_ally == n*n:
        break
    # myhash1[i]: i번째 동맹의 총 인구 수
    myhash1 = {}
    # myhash2[i]: i번째 동맹의 도시 수
    myhash2 = {}
    # myhash3[i]: i번째 동맹의 위치 (i,j)
    myhash3 = {}
    for i in range(1,num_ally+1):
        myhash1[i] = 0
        myhash2[i] = 0
        myhash3[i] = []
    # ally 정보 바탕으로 업데이트
    for i in range(n):
        for j in range(n):
            myhash1[ally[i][j]] += A[i][j]
            myhash2[ally[i][j]] += 1
            myhash3[ally[i][j]].append((i,j))
    # 인구이동
    for i in range(1,num_ally+1):
        moving_population = floor(myhash1[i] / myhash2[i])
        for loc in myhash3[i]:
            x,y = loc
            A[x][y] = moving_population
    answer += 1

print(answer)