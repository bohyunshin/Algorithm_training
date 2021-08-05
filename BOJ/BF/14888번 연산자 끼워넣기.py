n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cal = []
for index,c in enumerate(B):
    if c != 0:
        for _ in range(c):
            if index == 0:
                cal.append('+')
            if index == 1:
                cal.append('-')
            if index == 2:
                cal.append('*')
            if index == 3:
                cal.append('/')

def calculation(op,num):
    answer = num[0]
    num = num[1:]
    for i in range(len(op)):
        if op[i] == '+':
            answer += num[i]
        if op[i] == '-':
            answer -= num[i]
        if op[i] == '*':
            answer *= num[i]
        if op[i] == '/':
            if answer < 0:
                answer = -(abs(answer) // num[i])
            else:
                answer = answer // num[i]
    return answer

c = [False]*len(cal)
a = [0]*(n-1)
MIN = 1e100
MAX = -1e100

def go(index,n,m):
    global MAX
    global MIN
    if index == n:
        answer = calculation(a,A)
        if MAX < answer:
            MAX = answer
        if MIN > answer:
            MIN = answer
        # print(' '.join(list(map(str,a))))
        return
    for i in range(m):
        if c[i]:
            continue
        c[i] = True
        a[index] = cal[i]
        go(index+1,n,m)
        c[i] = False
# go(0,n-1,len(cal))
# print(MAX)
# print(MIN)

def go2(A,index,val,plus,minus,mul,div):
    global MIN
    global MAX
    if index == n-1:
        if MIN > val:
            MIN = val
        if MAX < val:
            MAX = val
        return
    if plus > 0:
        go2(A, index + 1, val + A[index], plus - 1, minus, mul, div)
    if minus > 0:
        go2(A, index + 1, val - A[index], plus, minus - 1, mul, div)
    if mul > 0:
        go2(A, index + 1, val * A[index], plus, minus, mul - 1, div)
    if div > 0:
        if val < 0:
            go2(A, index + 1, -(abs(val) // A[index]), plus, minus, mul, div - 1)
        else:
            go2(A, index + 1, val // A[index], plus, minus, mul, div - 1)
val = A[0]
A = A[1:]
go2(A,0,val,B[0],B[1],B[2],B[3])
print(MAX)
print(MIN)