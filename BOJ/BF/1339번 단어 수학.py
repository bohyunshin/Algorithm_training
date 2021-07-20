from itertools import permutations
n = int(input())
str_list = []
str_list_expand = []
num_loc = []
for _ in range(n): # O(N)
    a = input()
    str_list.append(a)
    str_list_expand += [i for i in a]
    num_loc.append(len(str_list_expand)-1)
k = len(set(str_list_expand)) # O(1)
str_list_expand = list(set(set(str_list_expand)))
nums = [i for i in range(10)][::-1]
answer = -1

# print(str_list)
# print(str_list_expand)
# print(num_loc)

for p in permutations(nums, k): # O(10!) = 400만
    myhash = {}
    for i in range(k):
        myhash[str_list_expand[i]] = p[i]
    temp = 0
    for s in str_list: # O(10^2)
        convert = ''
        for i in s:
            convert += str(myhash[i])
        temp += int(convert)
    if answer < temp:
        answer = temp
print(answer)