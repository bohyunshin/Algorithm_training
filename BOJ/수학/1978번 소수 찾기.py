n = int(input())
A = list(map(int, input().split()))
answer = []

def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
answer = 0
for i in A:
    if is_prime(i):
        answer += 1
print(answer)