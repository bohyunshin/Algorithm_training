from itertools import permutations
n = int(input())
innings = []
ans = 0
for _ in range(n):
    innings.append(list(map(int,input().split())))
# candis = [i for i in range(1,9)]
# for p in permutations(candis,len(candis)):
#     # if p[3] != 0:
#     #     continue
#     p = list(p)
#     p = p[:3] + [0] + p[3:]
#     score = 0
#     order = p[0]
#     total_order = {}
#     for i in range(len(p)):
#         if i == len(p)-1:
#             total_order[p[i]] = p[0]
#         else:
#             total_order[p[i]] = p[i+1]
#     rest = [0]*3
#     out = 0
#     for inning in innings:
#         while out <= 2:
#             player = inning[order]
#             # 아웃이면, 바로 아웃시키고 다음 타자 대기시킴.
#             if player == 0:
#                 out += 1
#                 order = total_order[order]
#                 continue
#             # 아웃아니면 잔루주자 포함하여 타자들을 진루시킴.
#             for i in range(len(rest) - 1, -1, -1):
#                 if rest[i] == 0:
#                     continue
#                 if i+player >= len(rest):
#                     score += 1
#                 else:
#                     rest[i+player] = 1
#                 rest[i] = 0
#             if player == 4:
#                 score += 1
#             else:
#                 rest[player-1] = 1
#             order = total_order[order]
#         # 이닝 끝.
#         out = 0
#         rest = [0]*3
#     ans = max(ans,score)
# print(ans)
# #

def simulate():
    score = 0
    order = player[0]
    total_order = {}
    for i in range(len(player)):
        if i == len(player) - 1:
            total_order[player[i]] = player[0]
        else:
            total_order[player[i]] = player[i + 1]
    rest = [0] * 3
    out = 0
    for inning in innings:
        while out <= 2:
            many = inning[order]
            # 아웃이면, 바로 아웃시키고 다음 타자 대기시킴.
            if many == 0:
                out += 1
                order = total_order[order]
                continue
            # 아웃아니면 잔루주자 포함하여 타자들을 진루시킴.
            for i in range(len(rest) - 1, -1, -1):
                if rest[i] == 0:
                    continue
                if i + many >= len(rest):
                    score += 1
                else:
                    rest[i + many] = 1
                rest[i] = 0
            if many == 4:
                score += 1
            else:
                rest[many - 1] = 1
            order = total_order[order]
        # 이닝 끝.
        out = 0
        rest = [0] * 3
    return score

player = [0]*9
check = [False]*9
def go(index):
    if index == 9:
        return simulate()
    if index == 3:
        player[index] = 0
        return go(index+1)
    ans = 0
    for i in range(1,9):
        if check[i]:
            continue
        check[i] = True
        player[index] = i
        temp = go(index+1)
        if ans < temp:
            ans = temp
        check[i] = False
        player[index] = 0
    return ans

print(go(0))
