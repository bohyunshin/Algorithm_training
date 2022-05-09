n = int(input())
a = list(int(i) for i in input())
b = list(int(i) for i in input())
a_cp = a.copy()
ans = 1e100
for i in range(2):
    a = a_cp.copy()
    tmp = 0
    if i == 0:
        a[0] = abs(a[0] - 1)
        a[1] = abs(a[1] - 1)
        tmp += 1
    for i in range(1,n):
        if a[i-1] == b[i-1]:
            pass
        else:
            tmp += 1
            if i == 0:
                a[i] = abs(a[i]-1)
                a[i+1] = abs(a[i+1]-1)
            elif i == n-1:
                a[i] = abs(a[i]-1)
                a[i-1] = abs(a[i-1]-1)
            else:
                a[i] = abs(a[i]-1)
                a[i-1] = abs(a[i-1]-1)
                a[i+1] = abs(a[i+1]-1)
    flag = False
    for i in range(n):
        if a[i] != b[i]:
            flag = True
            break
    if flag is False:
        ans = min(ans,tmp)
print(-1 if ans == 1e100 else ans)