import sys
input = sys.stdin.readline
n = int(input())
a = [-1] + list(map(int,input().split()))
s = [0]*(n+1)
for i in range(1,n+1):
    mistake = 1 if a[i-1] > a[i] else 0
    s[i] = s[i-1] + mistake
# print(s)
q = int(input())
for _ in range(q):
    x,y = map(int,input().split())
    print(s[y] - s[x])