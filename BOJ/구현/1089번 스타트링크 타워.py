from itertools import combinations
given =[
    '###...#.###.###.#.#.###.###.###.###.###',
    '#.#...#...#...#.#.#.#...#.....#.#.#.#.#',
    '#.#...#.###.###.###.###.###...#.###.###',
    '#.#...#.#.....#...#...#.#.#...#.#.#...#',
    '###...#.###.###...#.###.###...#.###.###'
        ]

def return_jeongoo(s):
    result = []
    x = y = 0
    while y != len(s[0])+1:
        tmp = [[0]*3 for _ in range(5)]
        for i in range(5):
            for j in range(3):
                tmp[i][j] = s[x+i][y+j]
        y += 4
        result.append(tmp)
    return result

def check(j1,j2):
    for i in range(5):
        for j in range(3):
            if j1[i][j] != j2[i][j]:
                return False
    return True

def return_turn_off_loc(jeongoo):
    result = []
    for i in range(5):
        for j in range(3):
            if jeongoo[i][j] == '.':
                result.append((i,j))
    return result

def recursive(index,m,lst):
    global answer,a,order,c
    if index >= m:
        answer.append(a[:])
        return
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i != index:
                continue
            if c[i][j] or order[i]:
                continue
            c[i][j] = True
            order[i] = True
            a[index] = lst[i][j]
            recursive(index+1,m,lst)
            c[i][j] = False
            order[i] = False

def main_recursive(lst):
    global answer,a,order,c
    n = len(lst)
    m = len(lst[0])
    answer = []
    a = [0]*n
    order = [False]*n
    c = [[False]*m for _ in range(n)]
    recursive(0,n,lst)
    return answer

nums = return_jeongoo(given)
n = int(input())
A = []
for _ in range(5):
    A.append(input())
jeongoos = return_jeongoo(A)
ans = [[] for _ in range(n)]
for index,jeongoo in enumerate(jeongoos):
    turn_off_loc = return_turn_off_loc(jeongoo)
    m = len(turn_off_loc)
    for i in range(m+1):
        for c in combinations(turn_off_loc,i):
            # 고장난 곳 불 켜보기.
            for x,y in c:
                jeongoo[x][y] = '#'
            # 0~9 전구랑 비교해보기.
            for cnt,num in enumerate(nums):
                if check(jeongoo,num):
                    ans[index].append(cnt)
            # 켜본 전구 다시 끄기.
            for x,y in c:
                jeongoo[x][y] = '.'
    if len(ans[index]) == 0:
        print(-1)
        exit()
candidate = main_recursive(ans)
final_ans = 0

for c in candidate:
    final_ans += int(''.join(list(map(str,c))))
print(final_ans / len(candidate))

"""
9
...................................
...................................
...................................
...................................
...................................
"""