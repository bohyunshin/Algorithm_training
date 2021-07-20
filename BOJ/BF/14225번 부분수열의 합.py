from itertools import combinations
n = int(input())
s = list(map(int, input().split()))
result = []
# 시간 복잡도는 nC1 + nC2 + ... + nCn = 2^n - 1
# 1048576 < 1억 -> 최악의 경우에도 2초 이내로 할 수 있음.
for k in range(1, len(s)+1):
    for c in combinations(s,k):
        result.append(sum(c))
result = list(set(result))
result.sort()
for idx, (i,j) in enumerate(zip(result, range(1, max(result)+1))):
    if i != j:
        print(j)
        break
    if idx == len(result)-1:
        print(len(result)+1)