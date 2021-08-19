n = int(input())
t = []
p = []
for _ in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)

a = [0]*n
answer = []

def solution(index,n):
    if index == n:
        answer.append(sum(a))
        return

    if index > n:
        return

    a[index] = p[index]
    solution(index+t[index],n)
    a[index] = 0
    solution(index+1,n)

def solution2(day,s):
    if day == n:
        answer.append(s)
        return
    if day > n:
        return

    solution2(day+t[day],s+p[day])
    solution2(day+1,s)

solution(0,n)
# solution2(0,0)
print(max(answer))