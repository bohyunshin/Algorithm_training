def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

def prev_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] >= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

def check(p,a):
    for i in range(len(a)):
        if a[i] == '>' and p[i] < p[i+1]:
            return False
        if a[i] == '<' and p[i] > p[i+1]:
            return False
    return True

k = int(input())
boodeungho = input().split()
nums = [str(i) for i in range(10)]

small = [i for i in range(k+1)]
big = [9-i for i in range(k+1)]

while True:
    if check(big, boodeungho):
        break
    if prev_permutation(big) is False:
        break
while True:
    if check(small, boodeungho):
        break
    if next_permutation(small) is False:
        break
print(''.join([str(i) for i in big]))
print(''.join([str(i) for i in small]))