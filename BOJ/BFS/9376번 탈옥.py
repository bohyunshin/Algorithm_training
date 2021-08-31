from collections import deque
def bfs(h,w,A,x,y):
    ans = []
    visited = [[-1]*w for _ in range(h)]
    door = [[[] for _ in range(w)] for _ in range(h)]
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = 0
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and A[nx][ny] != '*' and \
                (visited[nx][ny] == -1):
                #  or visited[nx][ny] > visited[x][y]+1 or visited[nx][ny] > visited[x][y]
                if A[nx][ny] == '#':
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
                    # if visited[nx][ny] > visited[x][y]+1:
                    #     door[nx][ny] = []
                    # door[nx][ny].clear()
                    door[nx][ny].append((nx,ny))
                    door[nx][ny] += door[x][y]
                if A[nx][ny] == '.':
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))
                    # if visited[nx][ny] > visited[x][y]:
                    #     door[nx][ny] = []
                    # door[nx][ny].clear()
                    door[nx][ny] += door[x][y]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                ans.append((x,y))
    # print(door[6][1],visited[6][1])
    # print(door[6][7],visited[6][7])
    # print(door[5][7],visited[5][7])
    # print(door[4][7],visited[4][7])
    # print(door[3][7],visited[3][7])
    return [door[x][y] for x,y in ans]

def solution(h,w,A):
    crimes = []
    for i in range(h):
        for j in range(w):
            if A[i][j] == '$':
                crimes.append((i,j))
                A[i][j] = '.'
    x, y = crimes[0]
    ans1 = bfs(h,w,A,x,y)
    x, y = crimes[1]
    ans2 = bfs(h, w, A, x, y)
    ans = 1e100
    for i in ans1:
        for j in ans2:
            l = len(set(i+j))
            if ans > l:
                ans = l
    # print(ans1)
    # print(ans2)
    return ans

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        h,w = map(int, input().split())
        A = []
        for _ in range(h):
            A.append([i for i in input()])
        print(solution(h,w,A))

"""
1
9 9
*#**#**#*
*#**#**#*
*#**#**#*
*#**.**#*
*#*#.#*#*
*$##*##$*
*#*****#*
*.......*
*********
"""