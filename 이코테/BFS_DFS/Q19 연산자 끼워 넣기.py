from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
add,minus,multi,divide = map(int, input().split())
operation = ['+']*add + ['-']*minus + ['*']*multi + ['/']*divide

lst = []

for p in permutations(operation):
    result = a[0]
    for index in range(1,len(a)):
        next_num = a[index]
        next_op = p[index-1]
        if next_op == '+':
            result += next_num
        elif next_op == '-':
            result -= next_num
        elif next_op == '*':
            result *= next_num
        else:
            if result < 0:
                result = -(abs(result) // next_num)
            else:
                result = result // next_num
    lst.append(result)
print(max(lst))
print(min(lst))