from collections import deque

def solution(f,s,g,u,d):
    visited = [-1]*(f+1)
    q = deque()
    visited[s] = 0
    q.append(s)
    dx = [u,-d]
    while q:
        x = q.popleft()
        if x == g:
            return visited[g]
        for i in range(2):
            nx = x + dx[i]
            if 1 <= nx < f+1 and visited[nx] == -1:
                visited[nx] = visited[x]+1
                q.append(nx)
    return 'use the stairs'

"""
0 <= nx < f+1에 대한 TC
4 1 4 4 1
-> 원래 정답은 못 내려감! 0층에 못가니까
근데 범위를 저렇게 잡으면 2로 답이 나옴. (1 -> 0 -> 4 경로)
"""

if __name__ == '__main__':
    f, s, g, u, d = map(int, input().split())
    print(solution(f,s,g,u,d))