from collections import defaultdict
n = int(input())
b = list(map(int,input().split()))
exist = defaultdict(bool)
for i in b:
    exist[i] = True
a = [0]*n
def go(index,n,before):
    if index == n:
        print(' '.join(map(str,a)))
        exit()
        return
    for i in range(n):
        if before == 0:
            a[index] = b[i]
            go(index+1,n,b[i])
        else:
            if (before % 3 == 0 and exist[before // 3] and before // 3 == b[i]) or (exist[before * 2] and before * 2 == b[i]):
                a[index] = b[i]
                go(index+1,n,b[i])
go(0,n,0)