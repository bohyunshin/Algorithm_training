n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(len(array[i])):
        # 왼쪽 위에서 올 경우
        if j == 0:
            left_up = 0
        else:
            left_up = array[i-1][j-1]
        # 오른쪽 위에서 올 경우
        if j == len(array[i])-1:
            right_up = 0
        else:
            right_up = array[i-1][j]
        array[i][j] = array[i][j] + max(left_up, right_up)
print(max(array[n-1]))

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""