n = 1000 - int(input())
moneys = [500,100,50,10,5,1]
ans = 0
for money in moneys:
    ans += n // money
    n = n % money
print(ans)