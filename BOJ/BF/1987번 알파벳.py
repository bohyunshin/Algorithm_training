from collections import defaultdict
r,c = map(int,input().split())
a = [input() for _ in range(r)]
visited = defaultdict(int)
check = [False]*26
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def go(x,y,check):
    ans = 0
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            ch = ord(a[nx][ny]) - ord('A')
            if check[ch] == False:
                check[ch] = True
                tmp = go(nx,ny, check)
                if ans < tmp:
                    ans = tmp
                check[ch] = False
    return ans+1
check[ord(a[0][0]) - ord('A')] = True
print(go(0,0,check))

# import sys
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# def go(board, check, x, y):
#     n = len(board)
#     m = len(board[0])
#     ans = 0
#     for k in range(4):
#         nx, ny = x+dx[k], y+dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             ch = ord(board[nx][ny])-ord('A')
#             if check[ch] == False:
#                 check[ch] = True
#                 temp = go(board, check, nx, ny)
#                 if ans < temp:
#                     ans = temp
#                 check[ch] = False
#     return ans+1
#
# n,m = map(int,sys.stdin.readline().split())
# board = [sys.stdin.readline().strip() for _ in range(n)]
# check = [False]*26
# check[ord(board[0][0])-ord('A')] = True
# print(go(board,check,0,0))