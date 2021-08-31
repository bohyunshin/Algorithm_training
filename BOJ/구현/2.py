ans = []
t = 'bbaa'

def recursive(s):
    print(s)
    if s == 'a':
        ans.append(t)
        return True
    if len(s) == 1 or len(s) == 0:
        return False

    if s[0] == 'a':
        recursive(s[1:])
    if s[-1] == 'a':
        recursive(s[:-1])
    cnt = 0
    for i, j in zip(s, s[::-1]):
        if i == j == 'b':
            cnt += 1
        else:
            break
    if cnt >= 1:
        recursive(s[(cnt):(-cnt)])

print(recursive('bba'))
print(ans)