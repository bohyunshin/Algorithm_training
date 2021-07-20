n = int(input())
A = []
# 메모리 터질거 대비해서 2차원으로만
# 이전것, 현재것만 담아둠.
dp_max = [[0]*3 for _ in range(2)]
dp_min = [[1e100]*3 for _ in range(2)]

if n == 1:
    row = list(map(int, input().split()))
    print(max(row), end=' ')
    print(min(row))
    exit(0)

for i in range(n):
    row = list(map(int, input().split()))

    # 처음에는 첫트 번째만 업데이트 함
    if i == 0:
        dp_max[0] = row.copy()
        dp_min[0] = row.copy()
        continue

    # 새로 들어온 애를 두 번째에 업데이트.
    dp_max[1] = row.copy()
    dp_min[1] = row.copy()

    # max, min 구하기
    for j in range(3):
        # max(바로 위에서 내려오는 것, 오른쪽 위에서 내려오는 것)
        if j == 0:
            dp_max[1][j] = max(dp_max[0][j] + row[j], dp_max[0][j+1] + row[j])
            dp_min[1][j] = min(dp_min[0][j] + row[j], dp_min[0][j + 1] + row[j])
        # max(왼쪽 위에서 내려오는 것, 바로 위에서 내려오는 것, 오른쪽 위에서 내려오는 것)
        elif j == 1:
            dp_max[1][j] = max(dp_max[0][j-1] + row[j], dp_max[0][j] + row[j], dp_max[0][j+1] + row[j])
            dp_min[1][j] = min(dp_min[0][j - 1] + row[j], dp_min[0][j] + row[j], dp_min[0][j + 1] + row[j])
        # max(바로 위에서 내려오는 것, 왼쪽 위에서 내려오는 것)
        else:
            dp_max[1][j] = max(dp_max[0][j] + row[j], dp_max[0][j-1] + row[j])
            dp_min[1][j] = min(dp_min[0][j] + row[j], dp_min[0][j - 1] + row[j])

    if i == n-1:
        break
    dp_max[0], dp_max[1] = dp_max[1], dp_max[0]
    dp_min[0], dp_min[1] = dp_min[1], dp_min[0]
print(max(dp_max[1]), end=' ')
print(min(dp_min[1]))