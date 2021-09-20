class Shark:
    def __init__(self, m, s, d):
        self.m = m
        self.s = s
        self.d = d
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

n, m, k = map(int, input().split())
a = [[[] for j in range(n)] for i in range(n)]
for _ in range(m):
    r,c,m,s,d = map(int, input().split())
    r -= 1
    c -= 1
    a[r][c].append(Shark(m,s,d))

for _ in range(k):
    b = [[[] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for shark in a[i][j]:
                x = i+dx[shark.d]*shark.s
                y = j+dy[shark.d]*shark.s
                x = (x % n + n) % n
                y = (y % n + n) % n
                b[x][y].append(shark)
    a = b
    for i in range(n):
        for j in range(n):
            if len(a[i][j]) > 1:
                total_m = 0
                total_s = 0
                cnt = len(a[i][j])
                compare_d = a[i][j][0].d % 2;
                result_d = 0;
                for shark in a[i][j]:
                    if shark.d % 2 != compare_d:
                        result_d = 1
                    total_m += shark.m
                    total_s += shark.s
                a[i][j].clear()
                shark_m = total_m // 5
                shark_s = total_s // cnt
                if shark_m > 0:
                    for direction in range(4):
                        a[i][j].append(Shark(shark_m, shark_s, direction*2+result_d))


ans = 0
for i in range(n):
    for j in range(n):
        for shark in a[i][j]:
            ans += shark.m
print(ans)