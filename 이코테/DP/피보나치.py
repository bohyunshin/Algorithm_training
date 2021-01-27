array = [0]*101
# 하향식 (탑다운)
def fib(x):
    if x == 1 or x == 2:
        return 1
    if array[x] != 0:
        return array[x]
    array[x] = fib(x-1) + fib(x-2)
    return array[x]

# 상향식 (보텀업)
array[1] = 1
array[2] = 1
n = 100
for i in range(3,n+1):
    array[i] = array[i-1] + array[i-2]
print(array[n])