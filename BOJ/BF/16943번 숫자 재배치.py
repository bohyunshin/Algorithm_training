a,b = map(int,input().split())
n = len(str(a))
A = [int(i) for i in str(a)]
num = [0]*n
c = [False]*n
ans = -1
def go(index,n):
    global ans
    if index == n:
        candi = int(''.join(map(str,num)))
        if candi < b and candi > ans:
            ans = candi
        return
    for i in range(n):
        if index == 0 and A[i] == 0:
            continue
        if c[i]:
            continue
        c[i] = True
        num[index] = A[i]
        go(index+1,n)
        c[i] = False
go(0,n)
print(ans)