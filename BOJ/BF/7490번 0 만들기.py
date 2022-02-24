t = int(input())
def go(index):
    if index == n-1:
        tmp = str(numbers[0])
        for i in range(n-1):
            # if a[i] != ' ':
            #     tmp += a[i]
            tmp += a[i]
            tmp += str(numbers[i+1])
        if eval(tmp.replace(' ','')) == 0:
            ans.append(tmp)
        return
    for i in range(len(cals)):
        a[index] = cals[i]
        go(index+1)
for _ in range(t):
    n = int(input())
    numbers = [i for i in range(1,n+1)]
    cals = ['+','-',' ']
    a = ['']*(n-1)
    ans = []
    go(0)
    ans.sort()
    for i in ans:
        print(i)
    print()
"""
10
1
2
3
4
5
6
7
8
9
9
"""