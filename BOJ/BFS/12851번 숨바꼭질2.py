from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)

n,k = map(int, input().split())
visited = [-1]*100001
q = deque()
q.append(n)
visited[n] = 0
myhash = {}

while q:
    x = q.popleft()

    if len(myhash.keys()) == 0:
        myhash[x] = x

    if x == k:
        break

    nxs = [x-1, x+1, 2*x]
    for nx in nxs:
        if 0 <= nx < len(visited):
            if visited[nx] == -1 or visited[nx] > visited[x] + 1:
                visited[nx] = visited[x] + 1
                q.append(nx)
                myhash[nx] = x

print(visited[k])
answer = []
if k % 2 == 0:
    nks = [k-1,k+1,k // 2]
else:
    nks = [k-1,k+1]
def get_result(k):

    if k not in myhash.keys():
        return -1

    answer = [k]
    while k != n:
        answer.append(myhash[k])
        try:
            k = myhash[k]
        except:
            return -1
    return ' '.join(map(str, answer[::-1]))

for nk in nks:
    a = get_result(nk)
    if a == -1:
        continue
    else:
        answer.append(a + ' ' + str(k))
print(len(answer))

