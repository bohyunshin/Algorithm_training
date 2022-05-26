a = [int(i) for i in input()]
tmp = 0
flag = False
for i in a:
    tmp += i
    if i == 0:
        flag = True
if not (tmp % 3 == 0 and flag == True):
    print(-1)
else:
    a.sort(reverse=True)
    print(''.join(map(str,a)))