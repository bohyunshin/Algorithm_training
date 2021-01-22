import sys
from collections import deque

n = int(input())

q = deque()
# queue에 들어가는 애들은 (현재 이모티콘 개수, 클립보드 이모티콘 개수)
q.append((1,0))

# 방문 확인용 visited dictionary는
# visited[key] = 걸린 시간
visited = {}
visited[(1,0)] = 0
path = []
while q:
    s,c = q.popleft()
    path.append((s,c))
    # 원하는 이모티콘 개수와 동일하다면
    if s == n:
        print(visited[(s,c)])
        print([path[i] for i in range(len(path)-1) if path])
        sys.exit()
    # 클립보드로 복사할건데, 만약에 아직 현재 이모티콘 상태에서
    # 현재 개수 이모티콘을 클립보드에 복사하지 않았다면
    if (s,s) not in visited.keys() and 1 <= s < 1001:
        visited[(s,s)] = visited[(s,c)] + 1
        q.append((s,s))
    if (s-1,c) not in visited.keys() and 1 <= s-1 < 1001 and 1 <= c <= 1001:
        visited[(s-1,c)] = visited[(s,c)] + 1
        q.append((s-1,c))
    if (s+c,c) not in visited.keys() and 1 <= s+c < 1001 and 1 <= c <= 1001:
        visited[(s+c,c)] = visited[(s,c)] + 1
        q.append((s+c,c))