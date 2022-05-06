from collections import deque
# def d(x):
#     x = int(x)
#     return str(2*x % 10000)
# def s(x):
#     x = int(x)
#     return str(9999) if x == 0 else str(x-1)
# def l(x):
#     if len(x) <= 3:
#         x = '0'*(4-len(x)) + x
#     x = [i for i in x]
#     x = x[1:] + [x[0]]
#     return str(int(''.join(x)))
# def r(x):
#     if len(x) <= 3:
#         x = '0'*(4-len(x)) + x
#     x = [i for i in x]
#     x = [x[-1]] + x[:-1]
#     return str(int(''.join(x)))
def d(x):
    return (2*x) % 10000
def s(x):
    return 9999 if x == 0 else x-1
def l(x):
    return 10*(x%1000) + x//1000
def r(x):
    return 1000*(x%10) + x//10
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    q = deque()
    visited = [-1]*10000
    q.append(a)
    visited[a] = ''
    funcs = [d,s,l,r]
    while q:
        x = q.popleft()
        if x == b:
            print(visited[x])
            break
        for func in funcs:
            nx = func(x)
            if visited[nx] == -1:
                visited[nx] = visited[x] + func.__name__.upper()
                q.append(nx)