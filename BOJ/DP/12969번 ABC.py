# n,K = map(int,input().split())
# MAX_k = int(n*(n-1)/2)
# dp = [[[] for _ in range(MAX_k+1)] for _ in range(n+1)]
# # 길이가 1인 애들 초기값 채워두기.
# dp[1][0] += ['A','B','C']
# for i in range(2,n+1):
#     for k in range(MAX_k+1):
#         # lst: ['AA','AB','AC']
#         lst = dp[i-1][k]
#         # j: 'AA'
#         for j in lst:
#             # 'A','B','C' 추가했을 때,
#             for add in ['A','B','C']:
#                 cnt = k
#                 for s in j:
#                     if s < add:
#                         cnt += 1
#                 dp[i][cnt].append(j+add)
#     for k in range(MAX_k+1):
#         tmp = sorted(dp[i][k])
#         if len(tmp) == 0:
#             continue
#         else:
#             dp[i][k] = [tmp[0]]
# print(-1 if len(dp[n][K]) == 0 else dp[n][K][0])

d = [[[[False]*436 for k in range(31)] for j in range(31)] for i in range(31)]
n, k = map(int,input().split())
ans = ''
def go(i, a, b, p):
    if i == n:
        if p == k:
            return True
        else:
            return False
    if d[i][a][b][p]:
        return False
    d[i][a][b][p] = True
    global ans
    temp = ans
    ans = temp + 'A'
    if go(i+1, a+1, b, p):
        return True
    ans = temp + 'B'
    if go(i+1, a, b+1, p+a):
        return True
    ans = temp + 'C'
    if go(i+1, a, b, p+a+b):
        return True
    return False
if go(0,0,0,0):
    # print(''.join(ans))
    print(ans)
else:
    print(-1)