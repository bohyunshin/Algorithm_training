n = 10
a = [list(map(int,input().split())) for _ in range(n)]
paper = [0,5,5,5,5,5]
def go(index,tmp):
    global ans
    if index == n**2:
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1:
                    return
        ans = min(ans,tmp)
        return
    row,col = index // n, index % n
    if a[row][col] == 1:
        for length in range(1,6):
            if paper[length] == 0:
                continue
            flag = 0
            for x in range(row,row+length):
                for y in range(col,col+length):
                    if 0 <= x < n and 0 <= y < n and a[x][y] == 1:
                        pass
                    else:
                        flag = 1
            if flag == 0:
                for x in range(row,row+length):
                    for y in range(col,col+length):
                        a[x][y] = 0
                paper[length] -= 1
                go(index+1,tmp+1)
                for x in range(row,row+length):
                    for y in range(col,col+length):
                        a[x][y] = 1
                paper[length] += 1
    else:
        go(index+1,tmp)
ans = 1e100
go(0,0)
print(-1 if ans == 1e100 else ans)