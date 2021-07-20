n = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)
group = 0
index = 0
while True:
    a = array[index]
    index += a
    group += 1

    if index >= len(array):
        break
print(group)