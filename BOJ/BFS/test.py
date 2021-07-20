def func(x):
    print(x)
    if x == 2:
        return '2입니당'
    else:
        for i in range(4):
            if func(i) == '2입니당':
                return '걸렸습니당'
    return '끝입니당'
print(func(3))