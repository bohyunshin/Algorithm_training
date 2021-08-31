n,c = map(int, input().split())
m = int(input())
box = []
for _ in range(m):
    x,y,z = map(int, input().split())
    box.append((x,y,z))
box.sort(key=lambda x: (x[1]))
capa = [c]*(n+1)
ans = 0
for i in range(m):
    temp = c
    for j in range(box[i][0],box[i][1]):
        temp = min(temp, capa[j])
    temp = min(temp, box[i][2])
    for j in range(box[i][0],box[i][1]):
        capa[j] -= temp
    ans += temp
print(ans)

# REF: https://steadev.tistory.com/15