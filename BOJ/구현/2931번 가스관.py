r,c = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
pipeline = {
    '|':[0,2], '-':[1,3], '+':[0,1,2,3],
    '1':[1,2], '2':[0,1], '3':[0,3], '4':[2,3],
    'M':[0,1,2,3], 'Z':[0,1,2,3]
}
a = [list(i for i in input()) for _ in range(r)]
gas = [[[] for _ in range(c)] for _ in range(r)]
a[1][3] = '-'
for i in range(r):
    for j in range(c):
        if a[i][j] == '.':
            continue
        elif a[i][j] in ['M', 'Z']:
            gas[i][j].append(a[i][j])
        else:
            gas[i][j] += pipeline[a[i][j]]
# for x in range(r):
#     for y in range(c):
#         if a[x][y] == '.':
#             for d in range(4):
#                 nx,ny = x+dx[d],y+dy[d]
#                 if 0 <= nx < r and 0 <= ny < c and len(gas[nx][ny]) >= 1:
#                     if d in gas[nx][ny]:
#                         for p in pipeline.keys():
#                             a[x][y] = p
#
#                             a[x][y] = '.'

def check(current,start,end):
    if current == end:
        return True
    x,y = current
    ans = False
    for d in pipeline[a[x][y]]:
        nx,ny = x+dx[d],y+dy[d]
        if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != '.':
            if d in gas[nx][ny]:
                return check((nx,ny),start,end)
    return ans

for i in range(r):
    for j in range(c):
        if a[i][j] == 'M':
            mos = (i,j)
        elif a[i][j] == 'Z':
            zag = (i,j)
for i in a:
    print(i)
print(check(mos,mos,zag))

# def check(x,y,from_,to_):
#     for d in pipeline[from_]:
#         nx,ny = x+dx[d],y+dy[d]
#         if d in pipeline[to_]:
#             return True
#     return False
# for i in range(r):
#     for j in range(c):
#         if a[i][j] == 'M':
#             mos = (i,j)
#         elif a[i][j] == 'Z':
#             zag = (i,j)
# def go(x,y,from_,ans):
#     if a[x][y] == 'Z':
#         return
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if 0 <= nx < r and 0 <= ny < c:
#             if a[nx][ny] == '.':
#                 if from_ == '.':
#                     continue
#                 for to_ in pipeline.keys():
