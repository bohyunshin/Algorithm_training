# n = int(input())
# array = list(map(int, input().split()))
#
# from itertools import combinations
#
# result = array.copy()
# m = 2
#
# while m <= n:
#     for c in combinations(array,m):
#         result.append(sum(c))
#     m += 1
# result = sorted(list(set(result)))
#
# nums = [i for i in range(1,max(result)+1)]
#
# print(min(set(nums)-set(result)))

n = int(input())
array = list(map(int, input().split()))

target = 1
for x in array:
    if x > target:
        break
    target += x
print(target)