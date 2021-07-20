n,m,k = map(int, input().split())
array = [int(i) for i in input().split()]
array.sort()

count = 0
result = 0

# while count != m:
#     if count % k == 0 and count != 0:
#         result += array[-2]
#     else:
#         result += array[-1]
#     count += 1
# print(result)

while True:
    for i in range(k):
        result += array[-1]
        m -= 1
        if m == 0:
            print(result)
            exit(0)
    result += array[-2]
    m -= 1
    if m == 0:
        print(result)
        exit(0)
