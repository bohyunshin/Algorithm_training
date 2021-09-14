def recursive(index,m,lst):
    global ans
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

a = [0]*3
order = [False]*3
c = [[False]*2 for _ in range(3)]
lst = [[(1,2),(3,4)],[(5,6),(7,8)],[(9,10),(11,12)]]
ans = []

recursive(0,3,lst)
for i in ans:
    print(i)