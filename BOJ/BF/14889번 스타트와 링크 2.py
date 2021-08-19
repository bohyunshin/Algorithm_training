import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
first = []
second = []
answer = 1e100
def solution(index,first,second):
    global answer
    if index >= n:
        if len(first) == n // 2 and len(second) == n // 2:
            t1 = 0
            t2 = 0
            for i in range(n//2):
                for j in range(n//2):
                    if i == j:
                        continue
                    t1 += s[first[i]][first[j]]
                    t2 += s[second[i]][second[j]]
            if abs(t1-t2) < answer:
                answer = abs(t1-t2)

    if len(first) > n // 2 or len(second) > n // 2:
        return

    first.append(index)
    solution(index+1,first,second)
    first.pop()

    second.append(index)
    solution(index+1,first,second)
    second.pop()
solution(0,first,second)
print(answer)