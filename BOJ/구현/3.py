from collections import deque
def bfs(B):
    n = len(B)
    FLAG = B[0] & B[1]
    for i in range(2,len(B)):
        FLAG = FLAG & B[i]
    if FLAG == 0:
        return 0
    q = deque()
    q.append(tuple(B))
    visited = {}
    visited[tuple(B)] = 0
    while q:
        B = q.popleft()
        cnt = visited[B]
        B = list(B)
        for i in range(len(B)):
            B[i] -= 1
            FLAG = B[0] & B[1]
            if FLAG == 0:
                return cnt + 1
            for j in range(2,len(B)):
                FLAG = FLAG & B[j]
                if FLAG == 0:
                    return cnt + 1
            q.append(tuple(B))
            visited[tuple(B)] = cnt + 1
            B[i] += 1
print(bfs([1,2]))