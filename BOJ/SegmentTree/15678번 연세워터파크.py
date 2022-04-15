from math import log2, ceil
import sys
input = sys.stdin.readline

def update(node, start, end, k, var):
    if start == end:
        tree[node] = var
        return
    if k <= (start+end) // 2:
        update(node*2, start, (start+end) // 2, k, var)
    else:
        update(node*2 + 1, (start+end) // 2 + 1, end, k, var)
    tree[node] = max(tree[node*2], tree[node*2 + 1])

def find(node, start, end, left, right):
    if right < start or end < left:
        return -1e100
    if left <= start and end <= right:
        return tree[node]
    return max(find(node*2, start, (start+end) // 2, left, right),
               find(node*2+1, (start+end)//2 + 1, end, left, right))

n,d = map(int,input().split())
l = list(map(int,input().split()))
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))
dp = [0]*n
for i in range(n):
    dp[i] = l[i]
    dp[i] = max(dp[i], l[i] + find(1, 0, n-1, max(0,i-d), i-1))
    # dp[i] = max(dp[i], l[i] + find(1, 0, n-1, i+1, min(i+d,n-1)))
    update(1,0,n-1,i,dp[i])
print(max(dp))