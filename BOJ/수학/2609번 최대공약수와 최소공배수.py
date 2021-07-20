n,m = map(int,input().split())

max_divider = max(n,m)
while True:
    if n % max_divider == 0 and m % max_divider == 0:
        break
    else:
        max_divider -= 1

print(max_divider)
print(max_divider * (n // max_divider) * (m // max_divider))