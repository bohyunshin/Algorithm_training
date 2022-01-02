from collections import defaultdict
def cum_sum(a):
    cum_total = 0
    for i in range(len(a)):
        cum_total += sum(a[:(i + 1)])
    return cum_total
t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    scores = list(map(int,input().split()))
    # history = [[[] for _ in range(m+1)] for _ in range(m+1) ]
    history = defaultdict(list)
    for score in scores:
        # history[1][score].append([score])
        history[(1,score)].append([score])

    for i in range(1,m):
        for j in range(m+1):
            if history[(i,j)] == []:
                continue
            for score in scores:
                for lst in history[(i,j)]:
                    tmp = cum_sum(lst + [score])
                    if tmp <= m:
                        history[(i+1,tmp)].append(lst + [score])
    ans = -1
    for i in range(1,m+1):
        for lst in history[(i,m)]:
            ans = max(ans,sum(lst))
    print(ans)