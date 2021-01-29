from itertools import combinations
a = 0
data = {}
while True:
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:
        break
    else:
        k = test_case[0]
        S = test_case[1:]
        data[a] = {}
        data[a]['k'] = k
        data[a]['S'] = S
        a += 1

for i in range(a):
    k = data[i]['k']
    S = data[i]['S']
    for c in combinations(S,6):
        print(' '.join(list(map(str,c))))

    if i != a-1:
        print('')