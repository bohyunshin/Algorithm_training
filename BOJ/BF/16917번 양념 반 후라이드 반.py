a,b,c,x,y = map(int,input().split())
total = 0
if a+b > c*2:
    if x >= 1 and y >= 1:
        while not (x == 0 or y == 0):
            total += c*2
            x -= 1
            y -= 1
        # total += x * a + y * b
        total = min(total + x * a + y * b, total + max(x,y)*2*c)
    else:
        total = min(x * a + y * b, max(x, y) * 2 * c)

else:
    total += x * a + y * b
print(total)