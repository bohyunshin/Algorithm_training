def recursive(index,m,lst):
    global ans,a,order,c
    if index >= m:
        ans.append(a[:])
        return
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i != index:
                continue
            if c[i][j] or order[i]:
                continue
            c[i][j] = True
            order[i] = True
            a[index] = lst[i][j]
            recursive(index+1,m,lst)
            c[i][j] = False
            order[i] = False

def main_recursive(lst):
    global ans,a,order,c
    n = len(lst)
    m = len(lst[0])
    ans = []
    a = [0]*n
    order = [False]*n
    c = []
    for i in range(n):
        c.append([False] * len(lst[i]))
    recursive(0,n,lst)
    return ans

lst = [[(1,2),(3,4)],[(5,6),(7,8)],[(9,10),(11,12)]]
ans = main_recursive(lst)
for i in ans:
    print(i)