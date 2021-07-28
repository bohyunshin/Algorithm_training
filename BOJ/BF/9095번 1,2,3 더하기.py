T = int(input())
def solution(count,s,n):
    if s > n:
        return 0
    if s == n:
        return 1
    now = 0
    for i in range(1,4):
        now += solution(count+1, s+i, n)
    return now

for _ in range(T):
    n = int(input())
    print(solution(0,0,n))
