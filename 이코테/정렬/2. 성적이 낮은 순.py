n = int(input())
array = []
for _ in range(n):
    tmp = input().split()
    name, grade = tmp[0], int(tmp[1])
    array.append( (name, grade) )

array.sort(key=lambda x: x[1])

for tup in array:
    print(tup[0], end= ' ')