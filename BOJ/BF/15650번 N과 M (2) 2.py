n,m = map(int, input().split())

c = [False]*(n+1)
a = [0]*m
def go(index,start,n,m):
    if index == m:
        print(' '.join(list(map(str,a))))
        return
    for i in range(start,n+1):
        a[index] = i
        go(index+1,i+1,n,m)

def go2(index,n,m):
    if index == m:
        print(' '.join(list(map(str,a))))
        return
    for i in range(1,n+1):
        if index >= 1 and a[index-1] > i:
            continue
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1,n,m)
        c[i] = False

go(0,1,n,m)