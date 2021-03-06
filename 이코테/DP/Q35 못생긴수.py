n = int(input())

result = [1,2,3,4,5]

candi = 6
while len(result) != n+1:
    candi_copy = candi
    for i in result[::-1]:
        if candi % i == 0:
            candi /= i

    for i in [2,3,5]:
        if candi % i == 0:
            candi /= i

    if candi == 1:
        result.append(candi_copy)
    candi = candi_copy + 1
print(result[n-1])