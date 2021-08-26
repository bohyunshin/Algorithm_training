from collections import deque, defaultdict
s,t = map(int, input().split())

if s == t:
    print(0)
    exit()
# visited = [0]*(max(s,t)+1)로 하니까 메모리 터졌음.
# 이렇게 하면 메모리는 10^9 * 4byte = 3810MB임!!.
visited = defaultdict(int)
q = deque()
visited[s] = 0
q.append(s)
cals = ['*','+','-','/']
myhash1 = {}
while q:
    x = q.popleft()
    if x == t:
        break
    for i in range(4):
        if cals[i] == '*':
            nx = x * x
        elif cals[i] == '+':
            nx = x + x
        elif cals[i] == '-':
            nx = x - x
        elif cals[i] == '/' and x != 0:
            nx = x // x
        if 0 <= nx <= t and visited[nx] == 0:
            visited[nx] = visited[x]+1
            myhash1[nx] = (x,cals[i])
            q.append(nx)
ans = ''
if visited[t] == 0:
    print(-1)
else:
    while t != s:
        ans += myhash1[t][1]
        t = myhash1[t][0]
    print(ans[::-1])