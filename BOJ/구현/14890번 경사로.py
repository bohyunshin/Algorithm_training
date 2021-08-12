n,l = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

def check(x):
    walls = [0]*len(x)
    FLAG = True
    for i in range(len(x)-1):
        # print(i)
        if x[i] == x[i+1]:
            continue
        else:
            if abs(x[i] - x[i+1]) >= 2:
                FLAG = False
                break
            # 작아지는 케이스라면.
            elif x[i] - x[i+1] == 1:
                if i+l >= len(x):
                    FLAG = False
                    break
                elif sum(walls[(i+1):(i+l+1)]) >= 1:
                    FLAG = False
                    break
                elif len(set(x[(i+1):(i+l+1)])) >= 2:
                    FLAG = False
                    break
                else:
                    for j in range(i+1,i+l+1):
                        walls[j] = 1
            # 커지는 케이스라면
            elif x[i] - x[i+1] == -1:
                if i+1-l < 0:
                    FLAG = False
                    break
                elif sum(walls[(i+1-l):(i+1)]) >= 1:
                    FLAG = False
                    break
                elif len(set(x[(i+1-l):(i+1)])) >= 2:
                    FLAG = False
                    break
                else:
                    for j in range(i+1-l,i+1):
                        walls[j] = 1
    return FLAG

def right_rotate(A):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][(n-1)-i] = A[i][j]
    return result
rotate_A = right_rotate(A)

answer = 0
for i in range(n):
    if check(A[i]):
        answer += 1
    if check(rotate_A[i]):
        answer += 1
print(answer)


