from collections import defaultdict
n = int(input())

dct = defaultdict(int)

for i in range(n):
    s = input()
    s = s[::-1]
    for i in range(len(s)):
        dct[s[i]] += 10**i
dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
number = 9
answer = 0
for x,y in dct:
    answer += number * y
    number -= 1
print(answer)