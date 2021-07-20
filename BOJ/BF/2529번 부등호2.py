from itertools import permutations

k = int(input())
boodeungho = input().split()
nums = [str(i) for i in range(10)]

result = []

max_val = -1e100
max_result = []
min_val = 1e100
min_result = []

# min 구하기
for p in permutations(nums,k+1):

    if min_val < int(''.join(p)):
        continue

    temp = 0
    for i in range(len(boodeungho)):
        if boodeungho[i] == '>':
            if p[i] > p[i+1]:
                temp += 1
            else:
                break
        if boodeungho[i] == '<':
            if p[i] < p[i+1]:
                temp += 1
            else:
                break
        # if eval(p[i] + boodeungho[i] + p[i+1]):
        #     temp += 1
        # else:
        #     break
    if temp == k:

        number = ''.join(p)

        if min_val > int(number):
            min_val = int(number)
            min_result = number
            break

# max 구하기
for p in permutations(nums[::-1],k+1):

    if int(''.join(p)) < max_val:
        continue

    temp = 0
    for i in range(len(boodeungho)):
        if boodeungho[i] == '>':
            if p[i] > p[i+1]:
                temp += 1
            else:
                break
        if boodeungho[i] == '<':
            if p[i] < p[i+1]:
                temp += 1
            else:
                break
        # if eval(p[i] + boodeungho[i] + p[i+1]):
        #     temp += 1
        # else:
        #     break
    if temp == k:

        number = ''.join(p)

        if max_val < int(number):
            max_val = int(number)
            max_result = number
            break

print(max_result)
print(min_result)