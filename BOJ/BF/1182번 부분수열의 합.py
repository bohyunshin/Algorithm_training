from itertools import combinations
n,s = map(int, input().split())
array = list(map(int, input().split()))
max_length = len(array)

count = 0
for k in range(1, max_length+1):
    for c in combinations(array,k):
        if sum(c) == s:
            count += 1
print(count)