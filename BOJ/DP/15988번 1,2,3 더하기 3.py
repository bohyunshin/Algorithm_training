import sys
sys.setrecursionlimit(10**6)
t = int(input())
def solution(x):
    if x == 0:
        return 1
    answer = 0
    if x < 0:
        return 0
    for i in range(1,4):
        answer += solution(x-i)
    return answer

for _ in range(t):
    n = int(input())
    print(solution(n))