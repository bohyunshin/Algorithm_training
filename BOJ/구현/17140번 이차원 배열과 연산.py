from collections import defaultdict
r,c,k = map(int, input().split())
r -= 1
c -= 1
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

def rotate(A):
    n = len(A)
    m = len(A[0])
    result = [[] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j].append(A[i][j])
    return result

def cal(A):
    result = []
    max_len = -1
    for i in range(len(A)):
        row = [i for i in A[i] if i != 0]
        dct = defaultdict(int)
        for j in row:
            dct[j] += 1
        temp = sorted([(val,cnt) for val,cnt in dct.items()], key=lambda x: (x[1], x[0]) )
        new_row = []
        for val,cnt in temp:
            new_row += [val,cnt]
        result.append(new_row)
        if max_len < len(new_row):
            max_len = len(new_row)

    for i in range(len(A)):
        if len(result[i]) < max_len:
            result[i] = result[i] + [0]*(max_len - len(result[i]))
    return result

time = 0
if len(A) <= r or len(A[0]) <= c:
    FLAG = True
elif A[r][c] != k:
    FLAG = True
else:
    FLAG = False

while FLAG:
    row = len(A)
    col = len(A[0])
    if row >= col:
        A = cal(A)
    else:
        rotate_A = rotate(A)
        A = rotate(cal(rotate_A))
    time += 1

    if len(A) <= r or len(A[0]) <= c:
        FLAG = True
    elif A[r][c] != k:
        FLAG = True
    else:
        FLAG = False

    if time > 100:
        print(-1)
        exit()
print(time)

