from copy import deepcopy
n,k = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
s,x,y = map(int,input().split())

is_check = [[0]*n for _ in range(n)]

da = [-1,1,0,0]
db = [0,0,-1,1]
time = 0

locs = {}
for i in range(n):
    for j in range(n):
        v = array[i][j]
        if is_check[i][j] == 1 or v == 0:
            continue
        try:
            locs[v].append((i, j))
            is_check[i][j] = 1
        except:
            locs[v] = []
            locs[v].append((i, j))
            is_check[i][j] = 1
next_locs = deepcopy(locs)

# 0초라면 현재 위치의 바이러스 출력
if s == 0:
    print(array[x-1][y-1])
    exit(0)

while True:
    locs = deepcopy(next_locs)
    next_locs = {}
    # 바이러스 번호를 작은 애부터 방문하기 위해서 오름차순 정렬
    keys_list = sorted(locs.keys())
    for v in keys_list:
        coords = locs[v]
        for c in coords:
            a,b = c
            for i in range(4):
                na = a + da[i]
                nb = b + db[i]
                if na < 0 or nb < 0 or na >= n or nb >= n:
                    continue
                # 바이러스가 퍼지지 않았다면
                if array[na][nb] == 0:
                    array[na][nb] = v

                    try:
                        next_locs[v].append((na,nb))
                    except:
                        next_locs[v] = []
                        next_locs[v].append((na, nb))
    time += 1

    if time == s:
        break
print(array[x-1][y-1])