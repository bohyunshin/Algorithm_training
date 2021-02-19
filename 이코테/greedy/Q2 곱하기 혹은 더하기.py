s = [int(i) for i in input()]

result = s[0]
for index, num in enumerate(s[1:]):
    if result == 0 or num == 0:
        result += num
    else:
        result *= num
print(result)
