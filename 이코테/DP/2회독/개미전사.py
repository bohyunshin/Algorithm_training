n = int(input())
s = list( map(int, input().split()) )
d = [0]*n

d[0] = s[0]
d[1] = max(s[0], s[1])
for i in range(2,n):
    d[i] = max( d[i-1], d[i-2] + s[i] )
print(max(d))