from collections import deque, defaultdict
n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(input())
for i in range(n):
    for j in range(m):
        if A[i][j] == 'B':
            B = (i,j)
        if A[i][j] == 'R':
            R = (i,j)
        if A[i][j] == 'O':
            H = (i,j)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = {}
q = deque()
visited[(R,B)] = 0
q.append((R,B))
answer = -1
while q:
    R,B = q.popleft()
    x_R, y_R = R
    x_B, y_B = B
    # 왼쪽으로 움직이기
    for i in range(4):
        nx_R, ny_R = x_R, y_R
        nx_B, ny_B = x_B, y_B
        # 벽 또는 구멍있는 곳까지 움직이기.
        while A[nx_R][ny_R] != '#' and A[nx_R][ny_R] != 'O':
            nx_R += dx[i]
            ny_R += dy[i]
        while A[nx_B][ny_B] != '#' and A[nx_B][ny_B] != 'O':
            nx_B += dx[i]
            ny_B += dy[i]
        # 빨간색 구슬만 구멍에 들어갔을 경우에 게임 끝!
        if (nx_R, ny_R) == H and (nx_B, ny_B) != H:
            ans = visited[((x_R,y_R), (x_B, y_B))] + 1
            if ans >= 11:
                print(-1)
            else:
                print(ans)
            exit()
        # 두 공 모두 구멍에 들어갔거나 파란 공이 구멍에 들어갔으면 실패니까 원점.
        if ((nx_R, ny_R) == H and (nx_B, ny_B) == H) or (nx_B, ny_B) == H:
            continue

        # 위 케이스 모두 아니라면 구멍이 아니라는 뜻이고 벽까지 갔다는 뜻이니까
        # 한칸 뒤로 물러섬.
        nx_R -= dx[i]
        ny_R -= dy[i]
        nx_B -= dx[i]
        ny_B -= dy[i]

        # 공이 겹쳐지면 안되니까 분리해야됨.
        if nx_R == nx_B and ny_R == ny_B:
            if i == 0: # 위쪽으로 이동하는 경우에,
                if x_R < x_B: # 빨간 구슬공이 파란 구슬공보다 위에 있었다면
                    nx_B -= dx[i] # 파란 구슬공을 아래로 한칸 옮김.
                else:
                    nx_R -= dx[i] # 반대의 경우에는 빨간 공을 아래로 한칸 옮김.
            if i == 1: # 아래쪽으로 이동하는 경우에,
                if x_R < x_B: # 빨간 구슬공이 파란 구슬공보다 위에 있었다면,
                    nx_R -= dx[i] # 빨간 구슬공을 위로 한칸 옮김
                else:
                    nx_B -= dx[i]
            if i == 2:
                if y_R < y_B:
                    ny_B -= dy[i]
                else:
                    ny_R -= dy[i]
            if i == 3:
                if y_R < y_B:
                    ny_R -= dy[i]
                else:
                    ny_B -= dy[i]

        # 여기까지 했으면 다음에 이동할 위치는
        # 로 정해짐.
        # 이제 하던대로 BFS 하면 됨.
        if ((nx_R, ny_R), (nx_B, ny_B)) not in visited.keys() or \
            visited[((nx_R, ny_R), (nx_B, ny_B))] > visited[((x_R, y_R), (x_B, y_B))] + 1:
            visited[((nx_R, ny_R), (nx_B, ny_B))] = visited[((x_R, y_R), (x_B, y_B))] + 1
            q.append(((nx_R, ny_R), (nx_B, ny_B)))

    #     break
    # break
if answer >= 11:
    print(-1)
else:
    print(answer)
