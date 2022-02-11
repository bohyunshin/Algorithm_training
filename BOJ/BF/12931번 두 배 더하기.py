# from collections import deque
# n = int(input())
# b = list(map(int,input().split()))
# a = [0]*n
# def key(l):
#     return ' '.join(map(str,l))
# def unkey(l):
#     return list(map(int,l.split(' ')))
# visited = {}
# q = deque()
# k = key(a)
# visited[k] = 0
# q.append(k)
# while q:
#     k = q.popleft()
#     unk = unkey(k)
#     if k == key(b):
#         print(visited[k])
#         break
#     for i in range(n):
#         unk[i] += 1
#         tmp = key(unk)
#         if visited.get(tmp) is None:
#             visited[tmp] = visited[k]+1
#             q.append(tmp)
#         unk[i] -= 1
#     unk = [i*2 for i in unk]
#     tmp = key(unk)
#     if visited.get(tmp) is None:
#         visited[tmp] = visited[k]+1
#         q.append(tmp)

n = int(input())
b = list(map(int,input().split()))
a = [0]*n
ans = 0
def check(l):
    for i in range(len(l)):
        if l[i] != 0:
            return True
    return False
while check(b):
    cnt = 0
    index = -1
    for i in range(n):
        if b[i]%2 == 0:
            cnt += 1
        else:
            if index == -1:
                index = i
    if cnt == n:
        for i in range(n):
            b[i] /= 2
    else:
        b[index] -= 1
    ans += 1
print(ans)
