from math import log2, ceil
import sys
input = sys.stdin.readline

def subsum(node, start, end, cnt):
    if start == end:
        return start
    # if node*2 <= tree_size and tree[node*2] >= cnt:
    #     return subsum(start, (start+end)//2, node*2, cnt)
    # cnt -= tree[node*2]
    # if node*2 + 1 <= tree_size and tree[node*2 + 1] >= cnt:
    #     return subsum((start+end)//2 + 1, end, node*2 + 1, cnt)
    if tree[node*2] >= cnt:
        return subsum(node*2, start, (start+end)//2, cnt)
    else:
        return subsum(node*2 + 1, (start+end)//2 + 1, end, cnt-tree[node*2])

def update(node, start, end, index, diff):
    if not (start <= index <= end):
        return
    tree[node] += diff
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2 + 1, (start+end)//2 + 1, end, index, diff)
MAX = 65537
n,k = map(int,input().split())
# h = int(ceil(log2(MAX)))
# tree = [0]*(2**(h+1))
tree = [0]*(MAX*4)
tree_size = len(tree)-1
l = [0]*(n+1)
ans = 0
for i in range(1,n+1):
    l[i] = int(input())
    update(1,0,MAX,l[i],1)
    if i >= k:
        x = subsum(1,0,MAX,(k+1)//2)
        ans += x
        update(1,0,MAX,l[i-k+1],-1)
print(ans)


"""
4 1
1
1
1
1

22 7
4
3
9
5
3
6
0
2
8
4
7
9
3
8
5
7
5
9
8
3
1
1
"""