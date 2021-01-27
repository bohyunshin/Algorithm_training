n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)

def binary_search(array, start, end):
    while start <= end:
        total = 0
        H = (start + end) // 2
        for x in array:
            if x > H:
                total += x-H
        if total == m:
            return H
        elif total < m:
            end = H-1
        else:
            start = H+1
            result = H
    return result
result = binary_search(array, start, end)
print(result)