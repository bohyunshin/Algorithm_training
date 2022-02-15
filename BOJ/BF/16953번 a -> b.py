from collections import deque
a,b = map(int,input().split())
def f1(x):
    return x*2
def f2(x):
    return x*10 + 1
funcs = [f1,f2]
q = deque()
visited = {}
q.append(a)
visited[a] = 0
while q:
    a = q.popleft()
    for func in funcs:
        na = func(a)
        if 1 <= na <= b and visited.get(na) == None:
            visited[na] = visited[a] + 1
            q.append(na)
print(visited[b]+1 if visited.get(b) != None else -1)