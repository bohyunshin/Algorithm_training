from itertools import combinations
n,m = map(int, input().split())
city = []
for _ in range(n):
    city.append( list(map(int, input().split())) )

chiken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i+1,j+1))
        elif city[i][j] == 2:
            chiken.append((i+1,j+1))

result = []
for i in range(1,m+1):
    for c in combinations(chiken, i):
        dist = 0
        for h in house:
            dist_house_ch = 1e10
            for ch in c:
                tmp = abs(ch[0]-h[0]) + abs(ch[1]-h[1])
                if dist_house_ch > tmp:
                    dist_house_ch = tmp
            dist += dist_house_ch
        result.append(dist)
print(min(result))