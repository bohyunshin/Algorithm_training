n,m = map(int, input().split())

result = {}
s = []
def f():
    if len(s) == m:
        # print(' '.join(map(str,s)))
        if ' '.join(sorted(map(str,s))) not in result.keys():
            result[' '.join(sorted(map(str,s)))] = 0
            print(' '.join(map(str, s)))
            return

    for i in range(1, n+1):
        if i in s:
            continue
        s.append(i)
        f()
        s.pop()
f()