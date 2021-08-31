n = int(input())
A = list(map(int, input().split()))
gori = [0]*n
A.sort()
if n == 2:
    print(1)
    exit()
index = 0
ans = 0
# 고리를 뒤부터 채운다.
for i in range(1,n):
    # 모두 채웠거나 더 이상 채울 고리가 없다면.
    if -i == -n or A[-i-1] == 0:
        break

    if A[index] == 0:
        index += 1
    gori[-i] += 1
    ans += 1
    A[index] -= 1

print(ans)

# TEST CASE
"""
4
3 4 5 7
>> 3
"""

"""
7
2 2 100 100 100 100 100
>> 4
"""