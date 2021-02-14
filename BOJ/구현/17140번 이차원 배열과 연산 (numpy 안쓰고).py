from collections import Counter
from copy import deepcopy
R,C,K = map(int, input().split())
R -= 1
C -= 1
A = []
for i in range(3):
    A.append( list(map(int, input().split())) )
time = 0

def transpose_list(lst):
    col = len(lst[0])
    lst_T = [[] for _ in range(col)]
    for i in lst:
        for j in range(col):
            lst_T[j].append(i[j])
    return lst_T

while True:

    try:
        if A[R][C] == K and time == 0:
            print(0)
            break
    except:
        pass

    trans_A = []
    row = len(A)
    col = len(A[0])
    time += 1

    max_len = 0
    if row >= col:
        for i in range(row):
            sort_list = []
            r = A[i]
            r = [t for t in r if t != 0]
            r_Counter = Counter(r)
            for k,v in r_Counter.items():
                sort_list.append((k,v))
            sort_list.sort(key=lambda x: (x[1],x[0]))
            new_row = [k for j in sort_list for k in j ]
            if max_len < len(new_row):
                max_len = len(new_row)
            trans_A.append(new_row)

        for i in range(row):
            if len(trans_A[i]) < max_len:
                trans_A[i] += [0]*(max_len - len(trans_A[i]))
        # tmp = [0]*max_len
        # for i in range(row):
        #     tmp = np.vstack([tmp, trans_A[i]])
        # trans_A = tmp[1:,:]
    else:
        A_t = transpose_list(A)
        for i in range(col):
            sort_list = []
            c = A_t[i]
            c = [t for t in c if t != 0]
            c_Counter = Counter(c)
            for k,v in c_Counter.items():
                sort_list.append((k,v))
            sort_list.sort(key=lambda x: (x[1],x[0]))
            new_row = [k for j in sort_list for k in j ]
            if max_len < len(new_row):
                max_len = len(new_row)
            trans_A.append(new_row)

        for i in range(col):
            if len(trans_A[i]) < max_len:
                trans_A[i] += [0]*(max_len - len(trans_A[i]))
        trans_A = transpose_list(trans_A)
    A = deepcopy(trans_A)

    try:
        if A[R][C] == K:
            print(time)
            break
    except:
        pass
    if time == 100:
        print(-1)
        break
