h,w = map(int,input().split())
if h == 1:
    print(1)
elif h == 2:
    print(min(4,(w+1)//2))
else:
    if w >= 7:
        print(w-2)
    else:
        print(min(4,w))

