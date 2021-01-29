from itertools import permutations
n = int(input())
A = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())
cal = ['+']*plus + ['-']*minus + ['*']*multiple + ['/']*divide

per_A = permutations(A)
per_cal = (permutations(cal))

def func(num, cal):
    result = num[0]
    num = num[1:]
    for i, (n, c) in enumerate(zip(num,cal)):
        if c == '+':
            result += num[i]
        elif c == '-':
            result -= num[i]
        elif c == '*':
            result *= num[i]
        else:
            if result > 0:
                result = result // num[i]
            else:
                result = -(abs(result) // num[i])
    return result
result = []
for i in per_A:
    for j in set(per_cal):
        result.append(func(i,j))

print(max(result))
print(min(result))