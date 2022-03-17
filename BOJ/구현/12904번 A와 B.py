# from collections import deque
#
# def func_1(x):
#     return x+'A'
# def func_2(x):
#     return x[::-1]+'B'
#
# s = input()
# t = input()
# visited = {}
# q = deque()
# funcs = [func_1,func_2]
# visited[s] = 0
# q.append(s)
# while q:
#     s = q.popleft()
#     if len(s) > len(t):
#         continue
#     for func in funcs:
#         ns = func(s)
#         if visited.get(ns) == None:
#             visited[ns] = visited[s] + 1
#             q.append(ns)
# if visited.get(t) == None:
#     print(0)
# else:
#     print(1)

s = input()
t = input()
while s != t:
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1][::-1]
    if len(s) > len(t):
        print(0)
        exit()
print(1)