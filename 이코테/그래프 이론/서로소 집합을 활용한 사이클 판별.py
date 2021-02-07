# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 함수를 호출함
    # 루트노드의 기준은 노드 번호 = 부모의 노드 번호
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        # a의 노드 번호가 작다면
        # b가 a를 바라보도록 = b의 부모 노드를 a로 정한다
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

cycle = False
# union 연산을 수행
for i in range(e):
    a,b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
    else:
        union_parent(parent, a, b)
print(cycle)
