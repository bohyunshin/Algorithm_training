R,C = 10,10
def move_shark(x,y,d,s):
    while s > 0:
        # 위
        if d == 1:
            if x == 1:
                d = 2
            elif x-1 >= s:
                x -= s
                s = 0
            elif x-1 < s:
                s -= x - 1
                x = 1
                d = 2
        # 아래.
        if d == 2:
            if R == x:
                d = 1
            elif R-x >= s:
                x += s
                s = 0
            elif R-x < s:
                s -= R - x
                x = R
                d = 1
        # 오른쪽.
        if d == 3:
            if C == y:
                d = 4
            elif C-y >= s:
                y += s
                s = 0
            elif C-y < s:
                s -= C-y
                y = C
                d = 4
        # 왼쪽.
        if d == 4:
            if y == 1:
                d = 3
            elif y-1 >= s:
                y -= s
                s = 0
            elif y-1 < s:
                s -= y-1
                y = 1
                d = 3
    return x,y,d
x,y,d = 1,9,2
x1,y1,d1 = 5,10,4
for _ in range(10):
    x,y,d = move_shark(x,y,d,8)
    x1,y1,d1 = move_shark(x1,y1,d1,7)
    print(x,y,d, 'hi', x1,y1,d1)