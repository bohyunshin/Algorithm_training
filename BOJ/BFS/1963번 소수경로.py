from collections import deque
from copy import deepcopy
def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

T = int(input())
test_case = []
for _ in range(T):
    test_case.append(input().split())

sieve_list = [i for i in prime_list(10000) if i >= 1000]

for i in range(T):
    _from = test_case[i][0]
    _to = test_case[i][1]
    start = int(_from)
    end = int(_to)

    if start == end:
        print(0)
        continue

    _from = [i for i in _from]
    _to = [i for i in _to]

    array = {i:0 for i in sieve_list}

    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        x = [i for i in str(x)]

        for k in range(4):
            if k == 0:
                to_change = [str(i) for i in range(1,10)]
            else:
                to_change = [str(i) for i in range(10)]
            to_change = [j for j in to_change if j != x[k]]

            for l in to_change:
                x_copy = deepcopy(x)
                x_copy[k] = l
                conv_num = int(''.join(x_copy))
                before_num = int(''.join(x))

                if conv_num in sieve_list and conv_num >= 1000:
                    if array[conv_num] == 0 or array[conv_num] > array[before_num] + 1:
                        array[conv_num] = array[before_num] + 1
                        q.append(conv_num)
    if array[end] == 0:
        print('Impossible')
    else:
        print(array[end])