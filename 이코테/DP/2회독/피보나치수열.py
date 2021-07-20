d = [0]*100
d[1] = 1
d[2] = 1
n = 99

# def fibonacci(x):
#     print(x)
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibonacci(x-1) + fibonacci(x-2)
#     return d[x]

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])

