n = 9
l = [2,1,3,7,5,9,4,8,1]
tree = [0]*31

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    tree[node] = init(node*2, start, (start+end)//2) + init(node*2 + 1, (start+end)//2 + 1, end)
    return tree[node]

init(1, 0, n-1)

print(tree)