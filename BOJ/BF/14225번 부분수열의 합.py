from itertools import combinations
n = int(input())
s = list(map(int, input().split()))
result = []
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