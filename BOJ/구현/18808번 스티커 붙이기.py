n,m,k = map(int,input().split())
cnt = 0
stickers = []
while cnt != k:
    cnt += 1
    r,c = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(r)]
    stickers.append(a)
def rotate(sticker):
    n,m = len(sticker), len(sticker[0])
    tmp = [[] for _ in range(m)]
    for j in range(m):
        for i in range(n):
            tmp[j].append(sticker[i][j])
        tmp[j] = tmp[j][::-1]
    return tmp
a = [[0]*m for _ in range(n)]
for sticker in stickers:
    is_attach = False
    r,c = len(sticker), len(sticker[0])
    for _ in range(4):
        for i in range(n):
            for j in range(m):
                cnt = 0
                attach_locs = []
                for k in range(r):
                    for l in range(c):
                        if 0 <= i+k < n and 0 <= j+l < m and \
                                a[i+k][j+l] + sticker[k][l] != 2:
                            attach_locs.append((k,l))
                            cnt += 1
                flag = True if r*c == cnt else False
                if flag:
                    for k,l in attach_locs:
                        a[i+k][j+l] += sticker[k][l]
                    break
            if flag:
                break
        if flag:
            break
        sticker = rotate(sticker)
        r,c = len(sticker), len(sticker[0])
    # for i in a:
    #     print(i)
    # print()
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            ans += 1
print(ans)