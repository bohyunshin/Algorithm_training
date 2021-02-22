from itertools import combinations
n,m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))
def chicken_distance(coord_house, coord_chicken):
    x = abs(coord_house[0] - coord_chicken[0])
    y = abs(coord_house[1] - coord_chicken[1])
    return x+y

result = []
for i in range(1,m+1):
    combi = combinations(chicken,i)
    for c in combi:
        city_chicken_dist = 0
        for h in house:
            chicken_dist = 1e10
            for ch in c:
                tmp = chicken_distance(h,ch)
                if chicken_dist > tmp:
                    chicken_dist = tmp
            city_chicken_dist += chicken_dist
        result.append(city_chicken_dist)
print(min(result))