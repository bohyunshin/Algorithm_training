t = int(input())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    x -= 1
    y -= 1
    k = x
    while k < n*m:
        if k%n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)




    # year = 1
    # a,b = (1,1)
    # FLAG = False
    # while not (x == a and y == b):
    #     a = (a+1)%(m+1) if a != m else 1
    #     b = (b+1)%(n+1) if b != n else 1
    #     year += 1
    #
    #     if m == a and n == b:
    #         if x == a and y == b:
    #             pass
    #         else:
    #             print(-1)
    #             FLAG = True
    #             break
    # if FLAG:
    #     continue
    # print(year)
    # # print(a,b)