n = int(input())
a = list(map(int,input().split()))
MIN,MAX = 1e100,-1e100
for i in a:
    if MIN > i:
        MIN = i
    if MAX < i:
        MAX = i
print(MIN,MAX)