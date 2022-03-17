row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
square = [[False]*10 for _ in range(9)]
seodoku = [list(int(i) for i in input()) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if seodoku[i][j] != 0:
            row[i][seodoku[i][j]] = True
            col[j][seodoku[i][j]] = True
            square[(i//3)*3 + (j//3)][seodoku[i][j]] = True

def go(cnt):
    if cnt == 81:
        for i in range(9):
            print(''.join(map(str,seodoku[i])))
        exit(0)
    x = cnt // 9
    y = cnt % 9
    if seodoku[x][y] == 0:
        for i in range(1,10):
            if row[x][i] == False and col[y][i] == False and \
                square[(x//3)*3 + (y//3)][i] == False:
                row[x][i] = col[y][i] = square[(x//3)*3 + (y//3)][i] = True
                seodoku[x][y] = i
                go(cnt+1)
                row[x][i] = col[y][i] = square[(x // 3) * 3 + (y // 3)][i] = False
                seodoku[x][y] = 0
    else:
        go(cnt+1)
go(0)