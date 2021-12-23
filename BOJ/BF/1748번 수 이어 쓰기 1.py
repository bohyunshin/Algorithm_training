t = int(input())
LEN = len(str(t))
ans = 0
while LEN != 0:
    f = 10**(LEN-1)
    ans += (t-f+1)*LEN

    # print(f,t)

    LEN -= 1
    t = 10**(LEN)-1
print(ans)