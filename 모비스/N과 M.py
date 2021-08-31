l,c = map(int, input().split())
s = input().split()
s.sort()
print(s)

def check(password):
    ja = 0
    mo = 0
    for s in password:
        if s in ['a','e','i','o','u']:
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1

def go(a,index,l):
    if len(a) == l:
        if check(a):
            print(a)
        return
    if index >= len(s):
        return
    go(a + s[index], index + 1, l)
    go(a,index+1,l)
go('',0,l)
