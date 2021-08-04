import sys
n = int(input())
b = 0

for _ in range(n):
    cal, *num = sys.stdin.readline().split()
    if len(num) > 0:
        num = int(num[0])-1
    if cal == 'add':
        b = b | (1 << num)
    if cal == 'check':
        if b & (1 << num) == 0:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write('1\n')
    if cal == 'remove':
        b = b & ~(1 << num)
    if cal == 'toggle':
        b = b ^ (1 << num)
    if cal == 'all':
        b = (1 << 20) - 1
    if cal == 'empty':
        b = 0
