numbers = []
for _ in range(9):
    numbers.append(int(input()))
n = len(numbers)
m = 7
c = [False]*n
a = [0]*m
def go(index,m):
    global ans
    if index == m:
        if sum(a) == 100:
            ans = a.copy()
        return
    for i in range(n):
        if c[i]:
            continue
        c[i] = True
        a[index] = numbers[i]
        go(index+1,m)
        c[i] = False
go(0,m)
ans.sort()
for i in ans:
    print(i)

# test