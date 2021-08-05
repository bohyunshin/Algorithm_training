n = int(input())
A = list(map(int, input().split()))
plus,minus,mul,div = map(int, input().split())

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
MAX = -1e100
MIN = 1e100
go2(A,0,val,plus,minus,mul,div)
print(MAX)
print(MIN)