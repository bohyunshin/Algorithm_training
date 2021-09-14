S = list(map(int, input().split()))
def make_dalpang(n):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    a = [[0]*n for _ in range(n)]
    x = y = 0
    # a[x][y] = n*n
    a[x][y] = 1
    k = 0
    for i in range(2,n*n+1):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 0:
            pass
        else:
            k = (k+1)%4
            nx,ny = x+dx[k],y+dy[k]
        a[nx][ny] = i
        x,y = nx,ny
    return a
def concat_rowwise(lst):
    # if len(A[0]) != len(B[0]):
    #     raise ValueError("Column length must be same")
    result = []
    for mat in lst:
        for row in mat:
            result.append(row)
    return result
def concat_colwise(lst):
    # if len(A) != len(B):
    #     raise ValueError("Row length must be same")
    n = len(lst[0])
    result = [[] for _ in range(n)]
    for mat in lst:
        for i in range(len(mat)):
            result[i] += mat[i]
    return result

dalpang = make_dalpang(S[0])
def recursive_dalpang(dalpang,S,index):
    if index >= len(S):
        return dalpang
    m = len(dalpang)
    next_s = S[index]
    dalpang_index = make_dalpang(next_s)
    dalpang_element = []
    dalpang_element.append(dalpang)
    n = next_s**2 - 1
    for cnt in range(n):
        tmp = [[0]*m for _ in range(m)]
        for j in range(m):
            for k in range(m):
                tmp[j][k] = dalpang[j][k] + m**2 * (cnt+1)
        dalpang_element.append(tmp)
    # return dalpang_element
    result = []
    for i in range(len(dalpang_index)):
        loc = dalpang_index[i]
        tmp = [dalpang_element[i-1] for i in loc]
        row = concat_colwise(tmp)
        result.append(row)
    final_result = concat_rowwise(result)

    return recursive_dalpang(final_result,S,index+1)

a = recursive_dalpang(dalpang,S,1)
for i in a:
    print(i)

