from itertools import combinations
n,s = map(int, input().split())
array = list(map(int, input().split()))
max_length = len(array)

count = 0
# 모든 combinations의 경우의 수를 세워봄
# 복잡도: sum_{n=1~20} nC1 + nC2 + ... + nCn = 210만 < 1억
for k in range(1, max_length+1):
    for c in combinations(array,k):
        if sum(c) == s:
            count += 1
print(count)