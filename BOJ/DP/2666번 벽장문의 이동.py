n = int(input())
a, b = map(int, input().split())
m = int(input())
order = []
for _ in range(m):
    order.append(int(input()))

dp = [0]*(n+1)
dp[a] += 1
dp[b] += 1

answer = 0
for i in order:
    if dp[i] == 1:
        continue
    temp = 999999
    door_close = 0
    for j in range(len(dp)):
        if dp[j] == 0:
            continue
        else:
            # print(i,j)
            if temp > abs(j-i):
                # answer += abs(j-i)
                door_close = j
                temp = abs(j-i)
    # print(i,door_close,temp)
    answer += abs(door_close - i)
    if door_close == 0:
        continue
    else:
        dp[door_close] -= 1
        dp[i] += 1
    # print(dp)
    # print()
print(answer)