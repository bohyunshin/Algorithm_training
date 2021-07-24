from collections import deque

s = int(input())
visited = [[-1]*(s+1) for _ in range(s+1)]
q = deque()
q.append((1,0))
visited[1][0] = 0

while q:
    x,clip = q.popleft()
    if x == s:
        break
    # 복사 후 클립보드 저장
    if visited[x][x] == -1 or visited[x][x] > visited[x][clip] + 1:
        visited[x][x] = visited[x][clip] + 1
        q.append((x,x))
    # 클립보드에 있는 이모티콘 붙여넣기
    if 0 <= x+clip < s+1:
        if visited[x+clip][clip] == -1 or visited[x+clip][clip] > visited[x][clip] + 1:
            visited[x + clip][clip] = visited[x][clip] + 1
            q.append((x+clip, clip))
    # 삭제할때
    if 0 <= x-1 < s+1:
        if visited[x-1][clip] == -1 or visited[x-1][clip] > visited[x][clip] + 1:
            visited[x-1][clip] = visited[x][clip] + 1
            q.append((x-1,clip))
print(min([i for i in visited[s] if i != -1]))

