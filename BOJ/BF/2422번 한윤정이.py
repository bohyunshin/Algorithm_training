n,m = map(int,input().split())
options = []
for _ in range(m):
    x,y = map(int,input().split())
    options.append((x,y))
a = [-1]*3
c = [False]*n
ans = 0
def go(index):
    global ans
    if index == 3:
        ans += 1
        print(a)
        return
    for i in range(n):
        if c[i]:
            continue
        ices = [j for j in a if j != -1]
        FLAG = False
        for option in options:
            x,y = option
            for ice in ices:
                # print(set([x,y]), set([ice,i]), set([x,y]) == set([ice,i]))
                if set([x,y]) == set([ice,i]):
                    FLAG = True
                    break
            if FLAG:
                break
        if FLAG == False:
            c[i] = True
            a[index] = i
            FLAG_ = FLAG
            go(index+1)
            c[i] = False
            FLAG = FLAG_
go(0)
print(ans)