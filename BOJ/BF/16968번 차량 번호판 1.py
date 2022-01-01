from string import ascii_lowercase
format = input()
numbers = [i for i in range(10)]
dct = {'c':ascii_lowercase, 'd':numbers}
ans = 0
a = ['']*len(format)
def go(index,m,before):
    global ans
    if index == m:
        ans += 1
        return
    s = dct[format[index]]
    for i in range(len(s)):
        now = s[i]
        if before == now:
            continue
        go(index+1,m,now)
go(0,len(format),'')
print(ans)