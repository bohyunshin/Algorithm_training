s = input()
t = input()
while s != t:
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1][::-1]
    if len(t) == 1:
        break
if s == t:
    print(1)
else:
    print(0)