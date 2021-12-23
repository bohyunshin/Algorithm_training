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


# t = int(input())
# def go(s, n):
#     global ans
#     if s == n:
#         ans += 1
#         return
#     if s > n:
#         return
#     for i in range(3):
#         s += numbers[i]
#         go(s, n)
#         s -= numbers[i]
# for _ in range(t):
#     n = int(input())
#     numbers = [1,2,3]
#     ans = 0
#     go(0,n)
#     print(ans)
