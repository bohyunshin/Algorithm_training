n,h = map(int,input().split())
bottom = [0]*(h+1)
top = [0]*(h+1)
a,b = 0,0
for i in range(n):
    if i % 2 == 0:
        bottom[int(input())] += 1
        a += 1
    else:
        top[int(input())] += 1
        b += 1
for i in range(1,h+1):
    bottom[i] += bottom[i-1]
    top[i] += top[i-1]
ans = -1
cnt = 0
for i in range(1,h+1):
    tmp = 0
    tmp += bottom[h] - bottom[i-1]
    tmp += top[h] - top[h-i]

    # print(bottom[h] - bottom[i-1], top[h] - top[h-i], cnt)

    if ans == -1 or ans > tmp:
        ans = tmp
        cnt = 1
    elif ans == tmp:
        # print(i)
        cnt += 1
print(ans, cnt)