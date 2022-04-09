from collections import defaultdict, Counter
from string import ascii_uppercase
alpha2num = {}
for i in range(10):
    alpha2num[str(i)] = i
num2alpha = {}
letters = [i for i in range(10)]
for i in range(len(ascii_uppercase)):
    alpha2num[ascii_uppercase[i]] = i+10
    num2alpha[i+10] = ascii_uppercase[i]
    letters.append(ascii_uppercase[i])

n = int(input())
uq = set()
numbers = []
for _ in range(n):
    tmp = list(i for i in input())
    numbers.append(tmp)
    for i in tmp:
        uq.add(i)
k = min(int(input()), len(uq))

def convert(numbers):
    ans = 0
    i = 0
    for number in numbers[::-1]:
        ans += (alpha2num[number]) * 36**i
        i += 1
    return ans

def unconvert(integer):
    ans = ''
    while integer >= 36:
        x,y = integer // 36, integer % 36
        if y <= 9:
            ans += str(y)
        else:
            ans += num2alpha[y]
        integer = x
    if integer <= 9:
        ans += str(integer)
    else:
        ans += num2alpha[integer]
    return ans[::-1]

convert_list = []
numbers_cp = numbers.copy()

while k > 0:
    convert_list_now = []
    dct = defaultdict(list)
    for number in numbers:
        dct[len(number)].append(number)
    lengths = sorted(list(dct.keys()), reverse=True)
    # start = 0
    length = lengths[0]
    tmp = dct[length] # ['GOOD', 'LUCK', 'HAVE']
    candis = []
    for l in tmp:
        candis.append(l[0]) # ['G', 'L', 'H']
    criteria = defaultdict(int)
    for number in numbers:
        for i,l in enumerate(number[::-1]):
            if l not in candis:
                continue
            criteria[l] += 36**i
    criteria = sorted([(alpha,val) for alpha,val in criteria.items()], \
                      key=lambda x: x[1], reverse=True)
    for alpha,cnt in criteria:
        if alpha not in candis:
            continue
        if alpha in convert_list:
            continue
        convert_list.append(alpha)
        convert_list_now.append(alpha)
        k -= 1
        if k == 0:
            break

    for i,number in enumerate(numbers):
        if len(number) == length and number[0] in convert_list:
            numbers[i] = number[1:]

print(numbers)
ans = 0
for number in numbers_cp:
    tmp = ''
    for i in number:
        if i in convert_list:
            tmp += 'Z'
        else:
            tmp += i
    # print(tmp)
    ans += convert(tmp)
print(unconvert(ans))
# print(ans,convert('1100TC85'))
