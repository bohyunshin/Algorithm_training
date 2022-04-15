from math import log2, ceil
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    left = init(node * 2, start, (start + end) // 2)
    right = init(node*2 + 1, (start+end)//2 + 1, end)
    if l[left] > l[right]:
        tree[node] = left
    else:
        tree[node] = right
    return tree[node]

def query(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return -1e100
    a = query(node*2, start, (start+end)//2, left, right)
    b = query(node*2 + 1, (start+end)//2 + 1, end, left, right)
    if a == -1e100:
        return b
    elif b == -1e100:
        return a
    else:
        if l[a] > l[b]:
            return a
        else:
            return b

def find(node, start, end, left, right):
    if right < start or end < left:
        return -1e100
    if left <= start and end <= right:
        return tree[node]
    return max(find(node*2, start, (start+end) // 2, left, right),
               find(node*2+1, (start+end)//2 + 1, end, left, right))

# def find_ans(start, end, subsum):
#     global ans
#     if not (0 <= start and end < n) or end < 0:
#         return
#     idx = query(1,0,n-1,start,end)
#     if idx == -1e100:
#         return
#     val = l[idx]
#     if val < 0:
#         ans = max(ans, subsum)
#     ans = max(ans, subsum+val)
#     find_ans(max(0,i-d), i-1, subsum+val)
    # if start < idx:
    #     val = max(ans, find_ans(start, idx-1))
    # if idx < end:
    #     val = max(ans, find_ans(idx+1, end))
    # return val

n,d = map(int,input().split())
l = list(map(int,input().split()))
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))
init(1,0,n-1)
ans = int(-1e100)
for i in range(n):
    tmp = l[i]
    idx = query(1, 0, n-1, max(0,i-d),i-1)
    if idx == -1e100:
        ans = max(ans,tmp)
        continue
    tmp = max(tmp, l[i] + l[idx])
    # if tmp == 37:
    #     print(i)
    #     print(query(1, 0, n-1, max(0,i-d),i-1))
    ans = max(ans, tmp)
print(ans)

# print(tree)