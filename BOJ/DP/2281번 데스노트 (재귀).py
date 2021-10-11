import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
people = []
for _ in range(n):
    people.append(int(input()))
dp = [[-1]*(m+2) for _ in range(n+1)]
def go(index,cnt):
    if index == n:
        return 0
    ans = dp[index][cnt]
    if ans != -1:
        return ans
    space = m-(cnt-1)
    cost = space**2
    # 다음 줄에 쓰는 경우.
    ans = go(index+1,people[index]+1) + cost
    if cnt + people[index] <= m:
        cur = go(index+1, cnt + people[index] + 1)
        if ans > cur:
            ans = cur
    dp[index][cnt] = ans
    return ans
print(go(1,people[0]+1))

for k in range(m+2):
    print(dp[n][k])