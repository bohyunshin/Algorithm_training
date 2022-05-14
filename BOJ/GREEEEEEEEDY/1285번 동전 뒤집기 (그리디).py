import sys
sys.setrecursionlimit(10**5)
n = int(input())
a = [list(i for i in input()) for _ in range(n)]
def change(coin):
    if coin == 'T':
        return 'H'
    else:
        return 'T'
ans = 1e100
def go(arr,idx):
    global ans
    if idx == n:
        for j in range(n):
            h, t = 0, 0
            for i in range(n):
                if arr[i][j] == 'H':
                    h += 1
                else:
                    t += 1
            if t > h:
                for i in range(n):
                    arr[i][j] = change(arr[i][j])
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'T':
                    cnt += 1
        ans = min(ans,cnt)
        return
    # 행 바꾸기.
    for j in range(n):
        arr[idx][j] = change(arr[idx][j])
    go(arr,idx+1)
    # 원래대로.
    for j in range(n):
        arr[idx][j] = change(arr[idx][j])
    # 행 바꾸지 않기.
    go(arr,idx+1)
go(a,0)
print(ans)
"""
3
TTT
TTT
TTT
"""
# ans = 1e100
# def go(arr):
#     global ans
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 'T':
#                 cnt += 1
#     ans = min(ans,cnt)
#     for i in range(n):
#         t,h = 0,0
#         for j in range(n):
#             if arr[i][j] == 'T':
#                 t += 1
#             else:
#                 h += 1
#         if t >= h:
#             for j in range(n):
#                 if arr[i][j] == 'T':
#                     arr[i][j] = 'H'
#                 else:
#                     arr[i][j] = 'T'
#             go(arr)
#             for j in range(n):
#                 if arr[i][j] == 'T':
#                     arr[i][j] = 'H'
#                 else:
#                     arr[i][j] = 'T'
#
#     for j in range(n):
#         t,h = 0,0
#         for i in range(n):
#             if arr[i][j] == 'T':
#                 t += 1
#             else:
#                 h += 1
#         if t >= h:
#             for i in range(n):
#                 if arr[i][j] == 'T':
#                     arr[i][j] = 'H'
#                 else:
#                     arr[i][j] = 'T'
#             go(arr)
#             for i in range(n):
#                 if arr[i][j] == 'T':
#                     arr[i][j] = 'H'
#                 else:
#                     arr[i][j] = 'T'
# go(a)
# print(ans)