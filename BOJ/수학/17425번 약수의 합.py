n = 1000000
# d[i]: i의 약수의 합 = f(i)
d = [1]*(n+1)
# s[i]: i까지의 약수의 합 = g(i)
s = [0]*(n+1)
for i in range(2,n+1):
    answer = 0
    for j in range(1,n+1):
        # 배수인 애들은 무조건 약수임
        # -> 배수인 애들만 살펴봐서 복잡도를 줄임
        # j for문의 복잡도는 n/2 + n/3 + ... + n/n < logn + 1
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
