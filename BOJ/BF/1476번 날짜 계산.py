e,s,m = map(int,input().split())
a,b,c = [1,1,1]
year = 1
while not (a == e and b == s and c == m):
    a = (a+1)%16 if a != 15 else 1
    b = (b+1)%29 if b != 28 else 1
    c = (c+1)%20 if c != 19 else 1
    year += 1
print(year)