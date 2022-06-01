n,k = map(int,input().split())
k_ = k
MAX = 0
cnt = 1
base = 9
cum = 0
while True:
    tmp = cnt*base
    if tmp <= k:
        MAX += tmp
        cum += base
        k -= tmp
        cnt += 1
        base *= 10
    else:
        break
# print(MAX, cum)
base = base // 10 + 1
MAX = MAX + (n-cum)*(cnt)
if MAX < k_:
    print(-1)
else:
    tmp = MAX - (n-cum)*(cnt)
    diff = k_ - tmp
    div,mod = diff // cnt, diff % cnt
    last = cum+div
    # print(last,div,mod)
    if mod == 0:
        print(str(last)[-1])
    else:
        last += 1
        print(str(last)[mod-1])
# a = 0
# for i in range(1,101851+1):
#     a += len(str(i))
# print(a)

"""
101851 500001
"""