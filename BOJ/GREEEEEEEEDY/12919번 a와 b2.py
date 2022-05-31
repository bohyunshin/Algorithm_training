s = input()
t = input()
def go():
    global s,t
    if s == t:
        # print(s,t)
        print(1)
        exit()
        return
    if len(t) == 1:
        return
    if t[-1] == 'A':
        t = t[:-1]
        go()
        t = t + 'A'
        if t[0] == 'B':
            t = t[::-1]
            t = t[:-1]
            go()
            t = t + 'B'
            t = t[::-1]
    else:
        if t[0] == 'B':
            t = t[::-1]
            t = t[:-1]
            go()
            t = t + 'B'
            t = t[::-1]
go()
print(0)