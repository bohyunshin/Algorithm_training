n,k = map(int,input().split())
number = []
for _ in range(n):
    a = int(input())
    number.append(a)
number = list(set(number))
number.sort()
dp = [0]*(k+1)
dp[0] = 1
for j in range(len(number)):
    for i in range(1,k+1):
        if i-number[j] >= 0 and dp[i-number[j]] >= 1:
            tmp = dp[i-number[j]] + 1
            if dp[i] == 0 or dp[i] > tmp:
                dp[i] = tmp
print(dp[k]-1 if dp[k] != 0 else -1)
# for i in dp:
#     print(i)

"""
3 15
2
2
2
"""


# n,k = map(int,input().split())
# number = []
# for _ in range(n):
#     a = int(input())
#     number.append(a)
# number = list(set(number))
# number.sort()
# dp = [[] for _ in range(k+1)]
# dp[0].append(0)
# for j in range(len(number)):
#     for i in range(1,k+1):
#         if i-number[j] >= 0 and len(dp[i-number[j]]) != 0:
#             tmp = dp[i-number[j]][:] + [number[j]]
#             if len(dp[i]) == 0 or len(dp[i]) > len(tmp):
#                 dp[i] = tmp
# print(len(dp[k])-1 if len(dp[k]) != 0 else -1)