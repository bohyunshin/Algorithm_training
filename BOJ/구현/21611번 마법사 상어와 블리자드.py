from copy import deepcopy
n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
magic = []
for _ in range(m):
    d,s = map(int,input().split())
    magic.append((d-1,s))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
mid = n//2
ans_one = 0
ans_two = 0
ans_three = 0
# for i in A:
#     print(i)

def return_seq(A):
    vals = []
    x, y = (n // 2, n // 2)
    dx_ = [0, 1, 0, -1]
    dy_ = [-1, 0, 1, 0]
    k = 0
    LEN = 1
    while True:
        FLAG = False
        for _ in range(2):
            for _ in range(LEN):
                x += dx_[k]
                y += dy_[k]
                vals.append(A[x][y])
                if (x, y) == (0, 0):
                    FLAG = True
                    break
            k = (k + 1) % 4
            if FLAG:
                break
        if FLAG:
            break
        LEN += 1
    return vals

def magic_fill_in(A):
    vals = return_seq(A)
    new_vals = []
    for val in vals:
        if val != 0:
            new_vals.append(val)
    new_vals += [0]*(n**2-1-len(new_vals))

    # 다시 채워넣기.
    result = [[0]*n for _ in range(n)]
    x, y = (n // 2, n // 2)
    dx_ = [0, 1, 0, -1]
    dy_ = [-1, 0, 1, 0]
    k = 0
    LEN = 1
    index = 0
    while True:
        FLAG = False
        for _ in range(2):
            for _ in range(LEN):
                x += dx_[k]
                y += dy_[k]
                result[x][y] = new_vals[index]
                index += 1
                if (x, y) == (0, 0):
                    FLAG = True
                    break
            k = (k + 1) % 4
            if FLAG:
                break
        if FLAG:
            break
        LEN += 1
    return result

def magic_burn(A):
    global ans_one, ans_two, ans_three
    while True:
        vals = return_seq(A)
        burned = []
        cnt = 1
        before = vals[0]
        before_loc = [0]
        for i in range(1,len(vals)):
            if vals[i] == 0:
                break
            if vals[i] == before:
                cnt += 1
                before_loc.append(i)
            else:
                if cnt >= 4:
                    burned += before_loc
                before = vals[i]
                before_loc = [i]
                cnt = 1
        if cnt >= 4:
            burned += before_loc

        if len(burned) == 0:
            return A

        # 폭발한 구슬의 수 추가.
        for index in burned:
            if vals[index] == 1:
                ans_one += 1
            elif vals[index] == 2:
                ans_two += 1
            elif vals[index] == 3:
                ans_three += 1

        not_burned_ball = []
        for index,val in enumerate(vals):
            if index not in burned:
                not_burned_ball.append(val)
        not_burned_ball += [0] * (n ** 2 - 1 - len(not_burned_ball))
        # 다시 채워넣기.
        result = [[0] * n for _ in range(n)]
        x, y = (n // 2, n // 2)
        dx_ = [0, 1, 0, -1]
        dy_ = [-1, 0, 1, 0]
        k = 0
        LEN = 1
        index = 0
        while True:
            FLAG = False
            for _ in range(2):
                for _ in range(LEN):
                    x += dx_[k]
                    y += dy_[k]
                    result[x][y] = not_burned_ball[index]
                    index += 1
                    if (x, y) == (0, 0):
                        FLAG = True
                        break
                k = (k + 1) % 4
                if FLAG:
                    break
            if FLAG:
                break
            LEN += 1
        A = deepcopy(result)

def magic_change(A):
    vals = return_seq(A)
    new_vals = []
    cnt = 1
    before = vals[0]
    before_loc = [0]
    for i in range(1, len(vals)):
        if vals[i] == 0:
            break
        if vals[i] == before:
            cnt += 1
            before_loc.append(i)
        else:
            new_vals.append(cnt)
            new_vals.append(before)
            before = vals[i]
            before_loc = [i]
            cnt = 1
    if i == 1 and before == 0:
        return A
    new_vals.append(cnt)
    new_vals.append(before)

    new_vals += [0] * (n ** 2 - 1 - len(new_vals))

    # 다시 채워넣기.
    result = [[0] * n for _ in range(n)]
    x, y = (n // 2, n // 2)
    dx_ = [0, 1, 0, -1]
    dy_ = [-1, 0, 1, 0]
    k = 0
    LEN = 1
    index = 0
    while True:
        FLAG = False
        for _ in range(2):
            for _ in range(LEN):
                x += dx_[k]
                y += dy_[k]
                result[x][y] = new_vals[index]
                index += 1
                if (x, y) == (0, 0):
                    FLAG = True
                    break
            k = (k + 1) % 4
            if FLAG:
                break
        if FLAG:
            break
        LEN += 1

    return result

for d,s in magic:
    nx,ny = mid,mid
    for _ in range(s):
        nx += dx[d]
        ny += dy[d]
        A[nx][ny] = 0
    A = magic_fill_in(A)
    A = magic_burn(A)
    A = magic_change(A)

# for i in A:
#     print(i)

print(ans_one + 2*ans_two + 3*ans_three)

"""
7 1
0 0 0 0 0 0 0
3 2 1 3 2 3 0
2 1 2 1 2 1 0
2 1 1 0 2 1 1
3 3 2 3 2 1 2
3 3 3 1 3 3 2
2 3 2 2 3 2 3
2 2

7 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
2 2

3 1
0 0 0
0 0 0
0 0 1
2 1

3 1
0 1 1
0 0 1
0 0 1
2 1
"""
