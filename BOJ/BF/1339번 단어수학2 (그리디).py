from collections import defaultdict
n = int(input())

dct = defaultdict(int)
# 문자별로 일의자리에 위치했는지, 십의자리에 위치했는지를
# dct에 담아둠
# 예시: GCF / ACDEB
# A -> 10**4
# B -> 10**0
# C -> 10**3 + 10**1
# D -> 10**2
# E -> 10*1
# F -> 10**0
for i in range(n): # O(10)
    s = input()
    s = s[::-1]
    for i in range(len(s)): # O(10) -> O(10^2)
        dct[s[i]] += 10**i
# 가장 큰 value을 가지는 dct의 key에 9를 부여함.
dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
number = 9
answer = 0
for x,y in dct:
    answer += number * y
    number -= 1
print(answer)
