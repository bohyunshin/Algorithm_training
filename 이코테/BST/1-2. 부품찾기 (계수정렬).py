n = int(input())
N = list(map(int, input().split()))
N.sort()
m = int(input())
M = list(map(int, input().split()))

array = [0]*1000001

for i in range(n):
    array[ N[i] ] += 1

for i in range(m):
    if array[ M[i] ] == 0:
        print('no',end=' ')
    else:
        print('yes',end=' ')