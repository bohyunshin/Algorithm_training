n = int(input())
l = list(map(int,input().split()))
ans = []
if len(l) == 1:
    print('A')
elif len(l) == 2:
    if l[0] == l[1]:
        print(l[0])
    else:
        print('A')
else:
    flag_same = 0
    for i in range(n-1):
        if l[i] == l[i+1] and l[i] != 0:
            flag_same = 1
    if flag_same == 1:
        if len(set(l)) == 1:
            print(l[0])
            exit()
        else:
            if l[0] == l[1]:
                print('B')
                exit()

    for k in [1,-1]:
        a = 0
        flag_over = 0
        while True:
            i = 0
            flag = 0
            x, y = l[i], l[i + 1]
            b = y - x * a
            while True:
                i += 1
                x, y = l[i], l[i + 1]
                if abs(x*a + b) > 100:
                    flag = 1
                    flag_over = 1
                    break
                if y == x*a + b:
                   pass
                else:
                   flag = 1
                if flag == 1 or i == n-2:
                    break
            if flag == 0:
                ans.append(l[-1]*a + b)
            if flag_over == 1:
                break
            a += k
    ans = list(set(ans))
    if len(ans) >= 2:
        print('A')
    elif len(ans) == 1:
        print(ans[0])
    else:
        print('B')
