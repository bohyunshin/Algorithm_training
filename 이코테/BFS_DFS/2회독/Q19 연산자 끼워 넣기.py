from itertools import product,permutations
n = int(input())
A = list(map(int, input().split()))
calculations = ['+','-','*','/']
B = list(map(int, input().split()))
C = []
result = []
for i,j in zip(calculations,B):
    C += [i]*j
for cals in permutations(C):
    value = A[0]
    for num, cal in zip(A[1:], cals):
        if cal == '+':
            value += num
        elif cal == '-':
            value -= num
        elif cal == '*':
            value *= num
        else:
            if value < 0:
                value = -(abs(value) // num)
            else:
                value = value // num
    result.append(value)
print(max(result))
print(min(result))