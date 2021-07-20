n = int(input())
w = int(input())
loc = []
for _ in range(w):
    loc.append( list(map(int,input().split())) )

dp = [[[] for _ in range(4)] for _ in range(w+1)]
dp[0] = [ [(1,1)], [(n,n)], [0], [[0]] ]

loc = [[0,0]] + loc
for i in range(1,w+1):
    x,y = loc[i]

    police1_new = []
    police2_new = []
    dist_new = []
    move_new = []
    for police1, police2, dist, move in zip( dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i-1][3] ):
        # police1 이동시키기
        police1_new.append((x,y))
        police2_new.append(police2)
        dist_new.append( dist + abs(x-police1[0]) + abs(y-police1[1]) )
        move_new.append(move + [1])

        # police2 이동시키기
        police1_new.append(police1)
        police2_new.append((x, y))
        dist_new.append(dist + abs(x - police2[0]) + abs(y - police2[1]))
        move_new.append(move + [2])

    dp[i][0] = police1_new
    dp[i][1] = police2_new
    dp[i][2] = dist_new
    dp[i][3] = move_new

    print(i)

min_index = dp[w][2].index(min(dp[w][2]))
print(dp[w][2][min_index])
for i in dp[w][3][min_index]:
    if i == 0:
        continue
    else:
        print(i)