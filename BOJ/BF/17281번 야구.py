from itertools import permutations
n = int(input())
innings = []
ans = 0
for _ in range(n):
    innings.append(list(map(int,input().split())))
for p in permutations(range(9),9):
    if p[3] != 0:
        continue
    # print(p)
    score = 0
    order = p[0]
    total_order = {}
    for i in range(len(p)):
        if i == len(p)-1:
            total_order[p[i]] = p[0]
        else:
            total_order[p[i]] = p[i+1]
    rest = [0]*4
    out = 0
    for inning in innings:
        while out <= 2:
            player = inning[order]
            # 아웃이면, 바로 아웃시키고 다음 타자 대기시킴.
            if player == 0:
                out += 1
                order = total_order[order]
                continue
            # 아웃아니면 잔루주자 포함하여 타자들을 진루시킴.
            for i in range(len(rest) - 1, -1, -1):
                rest[0] = 1
                if i + player >= len(rest):
                    if rest[i] == 1:
                        score += 1
                    rest[i] = 0
                else:
                    rest[i + player] = rest[i]
                    rest[i] = 0
                rest[0] = 0
            order = total_order[order]
        # 이닝 끝.
        out = 0
        # print(inning,order,score)
    # print(rest,score)
    # break
    ans = max(ans,score)
print(ans)
# rest = [0,1,1,0]
# player = 3
# score = 0
# out = 0
# for i in range(len(rest)-1,-1,-1):
#     if player == 0:
#         out += 1
#         continue
#     rest[0] = 1
#     if i+player >= len(rest):
#         if rest[i] == 1:
#             score += 1
#         rest[i] = 0
#     else:
#         rest[i+player] = rest[i]
#         rest[i] = 0
#     rest[0] = 0
# print(rest,score)



