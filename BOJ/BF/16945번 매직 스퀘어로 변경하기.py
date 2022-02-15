from itertools import permutations
n = 3
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
loc = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append((i,j))
    loc.append(tmp)
for j in range(n):
    tmp = []
    for i in range(n):
        tmp.append((i,j))
    loc.append(tmp)
loc.append([(0,0),(1,1),(2,2)])
loc.append([(0,2),(1,1),(2,0)])
def check():
    s = -1
    for l in loc:
        tmp = 0
        for x,y in l:
            tmp += b[x][y]
        if s == -1 or s == tmp:
            s = tmp
            pass
        else:
            return False
    return True
def dist():
    tmp = 0
    for i in range(n):
        for j in range(n):
            tmp += abs(a[i][j] - b[i][j])
    return tmp
m = 9
ans = -1
for p in permutations(range(1,10)):
    b = [[0]*n for _ in range(n)]
    for i in range(9):
        r,c = i // n, i % n
        b[r][c] = p[i]
    if check():
        cost = dist()
        if ans == -1 or ans > cost:
            ans = cost
print(ans)
# def go(index,start,from_,cost):
#     global ans
#     if index == m:
#         for i in a:
#             print(i)
#         print()
#         if check():
#             if ans == -1 or ans > cost:
#                 ans = cost
#         return
#     r,c = index // n, index % n
#     tmp = a[r][c]
#     for i in range(start,10):
#         for k in range(1,10):
#             a[r][c] = k
#             go(index+1,i+1,k+1,cost+abs(a[r][c] - k))
#             a[r][c] = tmp
# go(0,1,1,0)
# print(ans)