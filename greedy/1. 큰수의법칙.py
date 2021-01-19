input_ = "5 8 3\n2 4 5 4 6"

# 내 풀이
def law_of_large(x):
    N = int(x.split('\n')[0].split(' ')[0])
    M = int(x.split('\n')[0].split(' ')[1])
    K = int(x.split('\n')[0].split(' ')[2])

    array = [int(i) for i in x.split('\n')[1].split(' ')]
    array_sorted = sorted(array, reverse=True)

    max_val = 0
    current_how_many = 0

    times = M - current_how_many
    while current_how_many < M:

        if times > K:
            max_val += array_sorted[0]*K
            current_how_many += K
        else:
            max_val += array_sorted[1] * times
            current_how_many += times

        times = M - current_how_many

        print(max_val, current_how_many, times)

# 책 풀이 1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data = sorted(data)

first = data[-1]
second = data[-2]

result = 0
while True:
    for _ in range(k):
        result += first
        m -= 1
        if m == 0:
            break

    result += second
    m -= 1

    if m == 0:
        break
print(result)

# 책 풀이 2: fancy하게
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data = sorted(data)

first = data[-1]
second = data[-2]

result = 0

divided = m // (k+1)
rest = m % (k+1)
result += divided * (first*k + second)
chunk_list = [first for _ in range(k)] + [second]
result += sum(chunk_list[:rest])
print(result)

