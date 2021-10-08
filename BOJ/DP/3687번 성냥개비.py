cnt2num = {
    2:[1],
    3:[7],
    4:[4],
    5:[2,3,5],
    6:[6,9,0],
    7:[8]
}
dp_MAX = [-1e100]*(101)
cnt2num_max = dict()
for cnt in cnt2num.keys():
    cnt2num_max[cnt] = max(cnt2num[cnt])
# 초기값 설정.
for cnt in cnt2num_max.keys():
    dp_MAX[cnt] = cnt2num_max[cnt]
for i in range(2,101):
    if dp_MAX[i] != -1e100:
        current = dp_MAX[i]
        for cnt in cnt2num_max.keys():
            if i+cnt > 100:
                continue
            candidate = str(cnt2num_max[cnt]) + str(current)
            dp_MAX[i + cnt] = max(dp_MAX[i+cnt],int(candidate))

dp_MIN = [1e100]*(101)
cnt2num_min = dict()
for cnt in cnt2num.keys():
    cnt2num_min[cnt] = min(cnt2num[cnt])
# 초기값 설정.
for cnt in cnt2num_min.keys():
    dp_MIN[cnt] = cnt2num_min[cnt]
# 0으로 시작하면 안됨.
dp_MIN[6] = 6
for i in range(2,101):
    if dp_MIN[i] != 1e100:
        current = dp_MIN[i]
        for cnt in cnt2num_min.keys():
            if i+cnt > 100:
                continue
            candidate = str(current) + str(cnt2num_min[cnt])
            dp_MIN[i + cnt] = min(dp_MIN[i+cnt],int(candidate))
T = int(input())
for _ in range(T):
    x = int(input())
    print(dp_MIN[x], dp_MAX[x])