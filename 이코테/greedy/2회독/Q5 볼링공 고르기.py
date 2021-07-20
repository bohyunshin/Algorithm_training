n,m = map(int, input().split())
array = list(map(int, input().split()))

result = 0
multi = 1
array.sort()

for i in range(len(array)-1):
    count = ( len(array)-1 ) - i
    if array[i] != array[i+1]:
        result += count*multi
        multi = 1
    else:
        multi += 1
print(result)