import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
first = []
second = []
answer = -1
def solution(index,first,second):
    global answer
    if index == n:
        if len(first) > 0 and len(second) > 0:
            t1 = 0
            t2 = 0
            for i in range(len(first)):
                for j in range(len(first)):
                    if i == j:
                        continue
                    t1 += s[first[i]][first[j]]

            for i in range(len(second)):
                for j in range(len(second)):
                    if i == j:
                        continue
                    t2 += s[second[i]][second[j]]
            if abs(t1-t2) < answer or answer == -1:
                answer = abs(t1-t2)
        else:
            return

    if index > n:
        return

    solution(index+1,first + [index],second)
    solution(index+1,first,second + [index])
solution(0,first,second)
print(answer)