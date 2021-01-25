array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

sort_array = [0]*(max(array) + 1)

for i in range(len(array)):
    sort_array[ array[i] ] += 1

for i in range(len(sort_array)):
    for j in range(sort_array[i]):
        print(i, end=' ')