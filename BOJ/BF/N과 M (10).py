from collections import defaultdict
n,m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
dct = defaultdict(int)
a = [0]*m
c = [False]*n
def go(index,start,n,m):
    if index == m:
        key = ' '.join(list(map(str,a)))
        dct[key] += 1
        if dct[key] == 1:
            print(key)
        return
    for i in range(start,n):
        if c[i]:
            continue
        c[i] = True
        a[index] = A[i]
        go(index+1,i+1,n,m)
        c[i] = False
go(0,0,n,m)