from itertools import combinations
n,m = map(int, input().split())
weight = list(map(int, input().split()))

# result = 0
# for c in combinations(weight,2):
#     if len(set(c)) == 2:
#         result += 1
# print(result)

count = [0]*11
for i in weight:
    count[i] += 1
result = 0
for i in range(1,m+1):
    n -= count[i]
    result += count[i]*n
print(result)