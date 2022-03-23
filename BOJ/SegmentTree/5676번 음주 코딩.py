from math import log2, ceil
import sys
input = sys.stdin.readline

def get_sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def init(node, start, end):
    if start == end:
        tree[node] = get_sign(l[start])
        return tree[node]
    tree[node] = (init(node*2, start, (start+end)//2)) * \
                 (init(node*2 + 1, (start+end)//2 + 1, end))
    return tree[node]

def subsum(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return 1
    return ((subsum(node*2, start, (start+end)//2, left, right)) * \
           (subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)))

def update(node, start, end, index, old, new):
    if not (start <= index <= end):
        return
    elif start == end:
        tree[node] = get_sign(new)
        return

    update(node * 2, start, (start + end) // 2, index, old, new)
    update(node * 2 + 1, (start + end) // 2 + 1, end, index, old, new)

    tree[node] = tree[node*2] * tree[node*2 + 1]


while True:
    try:
        n,k = map(int, input().split())
    except:
        exit()
    h = int(ceil(log2(n)))
    tree = [0]*(2**(h+1))
    l = list(int(i) for i in input().split())
    ans = ''
    init(1, 0, n-1)
    for _ in range(k):
        cur = input().split()
        if cur[0] == 'C':
            _,i,new = cur
            i = int(i)
            new = int(new)
            old = l[i-1]
            update(1,0,n-1,i-1,old,new)
        else:
            _,i,j = cur
            i = int(i)
            j = int(j)
            tmp = subsum(1,0,n-1,i-1,j-1)
            if tmp == 1:
                ans += '+'
            elif tmp == -1:
                ans += '-'
            else:
                ans += '0'
    print(ans)

"""
8
0
1
2
3
4
5
6
7
"""