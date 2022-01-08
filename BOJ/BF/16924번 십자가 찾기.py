n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(input())
check = [[False]*m for _ in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            l = 0
            k = 1
            while True:
                if i+k < n and i-k >= 0 and j+k < m and j-k >= 0:
                    if a[i+k][j] == '*' and a[i-k][j] == '*' and a[i][j+k] == '*' and a[i][j-k] == '*':
                        l = k
                    else:
                        break
                else:
                    break
                k += 1
            if l > 0:
                ans.append((i+1,j+1,l))
                check[i][j] = True
                for k in range(1,l+1):
                    check[i+k][j] = True
                    check[i-k][j] = True
                    check[i][j+k] = True
                    check[i][j-k] = True
for i in range(n):
    for j in range(m):
        if a[i][j] == '*' and check[i][j] == False:
            print(-1)
            exit()
print(len(ans))
for p in ans:
    print(' '.join(map(str,p)))

# from collections import defaultdict
# from itertools import combinations
# n,m = map(int,input().split())
# A = []
# for _ in range(n):
#     A.append([i for i in input()])
# visited = [[False]*m for _ in range(n)]
# da = [0,1,0,-1]
# db = [1,0,-1,0]
# d = 0
# LEN = 1
# a,b = 1,1
# possible = []
# if a > n-1 or b > n-1:
#     ans = -1
# else:
#     c_a,c_b = a,b
#     while 0 <= c_a < n and 0 <= c_b < m:
#         a,b = c_a,c_b
#         while 0 <= a < n and 0 <= b < m:
#             cross = [(a, b)]
#             FLAG = False
#             for i in range(4):
#                 for k in range(1, LEN + 1):
#                     na, nb = a + da[i] * k, b + db[i] * k
#                     if 0 <= na < n and 0 <= nb < m:
#                         cross.append((na, nb))
#                     else:
#                         FLAG = True
#                         break
#                 if FLAG:
#                     break
#             # print(FLAG,cross)
#             if FLAG:
#                 a += 1
#                 b = c_b
#                 d = (d+1)%4
#             else:
#                 b += 1
#                 possible.append((cross,LEN))
#         c_a += 1
#         c_b += 1
#         LEN += 1
#
# def check(a,b):
#     n,m = len(a),len(a[0])
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] != b[i][j]:
#                 return False
#     return True
#
# FLAG = False
# for i in range(len(possible),0,-1):
#     for c in combinations(possible,i):
#         if len(c) > n*m:
#             continue
#         tmp = [['.']*m for _ in range(n)]
#         ans = []
#         for cross,l in c:
#             for x,y in cross:
#                 tmp[x][y] = '*'
#             ans.append((cross[0][0]+1,cross[0][1]+1,l))
#         if check(A,tmp):
#             print(len(ans))
#             for row in ans:
#                 print(' '.join(list(map(str,row))))
#             FLAG = True
#             break
#     if FLAG:
#         break
# if FLAG == False:
#     print(-1)

"""
6 8
....*...
...**...
..*****.
...**...
....*...
........

5 2
..
..
.*
..
..
"""