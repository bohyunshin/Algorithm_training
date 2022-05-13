import sys
sys.setrecursionlimit(10**5)
n = int(input())
a = [list(i for i in input()) for _ in range(n)]
ans = 1e100
def go(arr):
    global ans
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T':
                cnt += 1
    ans = min(ans,cnt)
    for i in range(n):
        t,h = 0,0
        for j in range(n):
            if arr[i][j] == 'T':
                t += 1
            else:
                h += 1
        if t >= h:
            for j in range(n):
                if arr[i][j] == 'T':
                    arr[i][j] = 'H'
                else:
                    arr[i][j] = 'T'
            go(arr)
            for j in range(n):
                if arr[i][j] == 'T':
                    arr[i][j] = 'H'
                else:
                    arr[i][j] = 'T'

    for j in range(n):
        t,h = 0,0
        for i in range(n):
            if arr[i][j] == 'T':
                t += 1
            else:
                h += 1
        if t >= h:
            for i in range(n):
                if arr[i][j] == 'T':
                    arr[i][j] = 'H'
                else:
                    arr[i][j] = 'T'
            go(arr)
            for i in range(n):
                if arr[i][j] == 'T':
                    arr[i][j] = 'H'
                else:
                    arr[i][j] = 'T'
go(a)
print(ans)