n,m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = 0
end = array[-1]
result = 0

while True:
    x = (start + end) // 2
    length = 0
    for i in array:
        if i > x:
            length += i-x

    if length > m:
        start = x-1
        result = x
    elif length == m:
        break
    else:
        end = x+1
print(x)
