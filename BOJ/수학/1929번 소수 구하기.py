m,n = map(int, input().split())
MAX = 1000000
check = [False]*(MAX+1)
check[0] = check[1] = True
for i in range(2, MAX+1):
    if check[i] is False:
        j = i*i
        while j <= MAX:
            check[j] = True
            j += i
for i in range(m,n+1):
    if check[i] is False:
        print(i)
