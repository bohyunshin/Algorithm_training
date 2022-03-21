m = 10000
check = [False]*(m+1)
def d(n):
    to_add = [n]
    for i in str(n):
        to_add.append(int(i))
    next_ = sum(to_add)
    if next_ <= m and check[next_] == False:
        check[next_] = True
        d(next_)
for i in range(1,m+1):
    d(i)
for i in range(1,m+1):
    if check[i] == False:
        print(i)