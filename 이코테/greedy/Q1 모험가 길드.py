n = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)

group = 0
index = 0

while True:
    start = array[index]
    index += start
    group += 1

    if index > len(array)-1:
        break

print(group)