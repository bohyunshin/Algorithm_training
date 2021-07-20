n = 1000000
d = [1]*(n+1)
s = [0]*(n+1)
for i in range(2,n+1):
    answer = 0
    for j in range(1,n+1):
        if i*j > n:
            break
        else:
            d[i*j] += i
s[1] = d[1]
for i in range(2,n+1):
    s[i] = s[i-1] + d[i]

answer = []
T = int(input())
for _ in range(T):
    n = int(input())
    answer.append(s[n])
print('\n'.join(map(str,answer)))
