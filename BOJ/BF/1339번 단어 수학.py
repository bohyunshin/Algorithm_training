from itertools import permutations
n = int(input())
str_list = []
str_list_expand = []
for _ in range(n): # O(N)
    a = input()
    str_list.append(a)
    str_list_expand += [i for i in a]
str_list_expand = list(set(str_list_expand))
k = len(str_list_expand)
nums = [i for i in range(10)][::-1]
answer = -1

# 총 복잡도는 O(10! * 10^2) = 4억 -> 브루트포스로하면 터질수밖에 없음.
for p in permutations(nums, k): # O(10!) = 400만
    myhash = {}
    for i in range(k):
        myhash[str_list_expand[i]] = p[i]
    temp = 0
    for s in str_list: # O(10)
        convert = ''
        for i in s: # O(10) -> O(10^2)
            convert += str(myhash[i])
        temp += int(convert)
    if answer < temp:
        answer = temp
print(answer)