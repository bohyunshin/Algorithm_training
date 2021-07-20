def check(key, lock):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if key[i][j]+lock[i][j] == 0 or key[i][j]+lock[i][j] == 2:
                return False
    return True

matrix = [[0,0,0], [0,0,0], [0,1,0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(lock[:2][:2])
