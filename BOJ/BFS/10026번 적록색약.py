import sys
sys.setrecursionlimit(10**6)

n = int(input())
array = []
for _ in range(n):
    array.append([i for i in input()])
array_patient = []
for j in range(n):
    array_patient.append( ['R' if i in ['R','G'] else 'B' for i in array[j]] )

visited = [[0]*n for _ in range(n)]

def dfs(array, visited, x, y, color):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    # color = array[x][y]
    if visited[x][y] == 0 and array[x][y] == color:
        visited[x][y] = 1

        dfs(array, visited, x-1, y, color)
        dfs(array, visited, x+1, y, color)
        dfs(array, visited, x, y-1, color)
        dfs(array, visited, x, y+1, color)

        return True
    else:
        return False
region = 0
region_patient = 0
for i in range(n):
    for j in range(n):
        if dfs(array, visited, i, j, array[i][j]) == True:
            region += 1
        if dfs(array_patient, visited, i, j, array_patient[i][j]) == True:
            region_patient += 1

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(array_patient, visited, i, j, array_patient[i][j]) == True:
            region_patient += 1
print(region, end=' ')
print(region_patient)
