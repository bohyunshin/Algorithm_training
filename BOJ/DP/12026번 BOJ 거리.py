from collections import defaultdict
n = int(input())
BOJ = ' ' + input()
s = 1
current = 'B'
dct = defaultdict(list)

for i in range(1,n+1):
    dct[BOJ[i]].append(i)

def what_is_next(current):
    if current == 'B':
        return 'O'
    if current == 'O':
        return 'J'
    if current == 'J':
        return 'B'
dp = [1e100]*(n+1)
dp[s] = 0
for i in range(1,n+1):
    if dp[i] != 1e100:
        current = BOJ[i]
        next_step = what_is_next(current)
        next_index = [j for j in dct[next_step] if j > i]
        for next in next_index:
            power = next-i
            dp[next] = min(dp[next],dp[i]+power**2)
print(-1 if dp[n] == 1e100 else dp[n])