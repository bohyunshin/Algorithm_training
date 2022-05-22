a = input()
if a[0] == '-':
    pass
else:
    a = '+' + a
num = []
cal = []
now = ''
for i in range(len(a)):
    if i != 0 and a[i] in ['+','-']:
        num.append(int(now))
        now = ''
    now += a[i]
num.append(int(now))
ans = 0
neg_flag = False
for i in range(len(num)):
    if i == 0:
        ans += num[i]
    else:
        if num[i] > 0:
            if neg_flag:
                ans += -num[i]
            else:
                ans += num[i]
        else:
            ans += num[i]
            neg_flag = True
print(ans)

"""
50-50+45-100
55-50+45+100
55-50-45-100
"""