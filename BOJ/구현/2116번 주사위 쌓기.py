n = int(input())
dice = []
for _ in range(n):
    dice.append(list(map(int,input().split())))
rotate = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
ans = -1
for i in range(6):
    result = []
    tmp = [1,2,3,4,5,6]
    tmp.remove(dice[0][i])
    next_ = dice[0][rotate[i]]
    tmp.remove(next_)
    result.append(max(tmp))
    for j in range(1,n):
        tmp = [1,2,3,4,5,6]
        tmp.remove(next_)
        idx = dice[j].index(next_)
        next_ = dice[j][rotate[idx]]
        tmp.remove(next_)
        result.append(max(tmp))

        # down = dice[j][next_]
        # idx = tmp.index(down)
        # tmp.remove(down)
        # next_ = dice[j][rotate[idx]]
        # tmp.remove(next_)
        # result.append(max(tmp))
    ans = max(ans,sum(result))
print(ans)



# dices = []
# for _ in range(n):
#     cur = list(map(int,input().split()))
#     dices.append(cur)
#     # d = {'h':cur[1:5], 'v':[cur[0], cur[2], cur[4], cur[5]]}
#     # dices.append(d)
# cur = dices[0]
# for i in range(6):
#     cur = [cur[-1]] + cur[:-1]
#     print(cur)