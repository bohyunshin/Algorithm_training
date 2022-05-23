n = int(input())
a = [int(input()) for _ in range(n)]
pos = []
neg = []
for i in range(len(a)):
    if a[i] >= 0:
        pos.append(a[i])
    else:
        neg.append(a[i])
pos.sort()
neg.sort()
now = len(pos)-1
ans = []
rest = []
# positive
while True:
    if now <= 0:
        break
    plus = pos[now] + pos[now-1]
    prod = pos[now] * pos[now-1]
    if prod > plus:
        ans.append(prod)
        now -= 2
    else:
        ans.append(pos[now])
        now -= 1
if now == 0:
    rest.append(pos[0])
# negative
now = 0
while True:
    if now >= len(neg)-1:
        break
    plus = neg[now] + neg[now+1]
    prod = neg[now] * neg[now+1]
    if prod > plus:
        ans.append(prod)
        now += 2
    else:
        ans.append(neg[now])
        now += 1
if now == len(neg)-1:
    rest.append(neg[-1])

if len(rest) == 0:
    print(sum(ans))
elif len(rest) == 1:
    print(sum(ans) + rest[0])
else:
    plus = rest[0] + rest[1]
    prod = rest[0] * rest[1]
    if prod >= plus:
        print(sum(ans) + prod)
    else:
        print(sum(ans) + plus)
# if now == 0:
#     ans.append(a[now])
# print(sum(ans))