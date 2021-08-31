from collections import defaultdict
n = int(input())
A = []
max_deadline = -1
for i in range(n):
    a,b= map(int, input().split())
    max_deadline = max(max_deadline,a)
    A.append((a,b))
A.sort(key=lambda x: (x[0],-x[1]))
c = [False]*n
days = [False]*(max_deadline+1)
work = [0]*(max_deadline+1)

ans = 0
for index,(d, cup) in enumerate(A):
    if days[d] == False and c[index] == False:
        ans += cup
        days[d] = c[index] = True
        work[d] = cup

# 사용하지 않은 일에 대해서 greedy하게 사용할 수 있는지 알아보기.
for i in range(1,len(days)):
    if days[i]:
        continue
    for index,(d,cup) in enumerate(A):
        if c[index] or d <= i:
            continue
        # 바로 첫번째 나오는 애가 greedy한 선택임.
        # 이미 정렬을 했으니까.
        ans += cup
        days[i] = c[index] = True
        work[i] = cup
        break
# 사용하지 않은 work에 대해서 greedy하게 사용할 수 있는지 알아보기.
# 사용하지 않은 work 이전 일에 대해서 걔보다 최소로 작은 애가 나오면 바로 바꿔주고 나오면 됨.
for i in range(n):
    if c[i]:
        continue
    d,cup = A[i]
    min_day = -1
    min_cup = 1e100
    for j in range(1,d):
        if work[j] < cup and min_cup > work[j]:
            min_cup = work[j]
            min_day = j
    if min_day != -1:
        work[min_day] = cup
print(sum(work))

# TEST CASE
"""
3
3 5
3 4
1 1
>> 10

7
1 9
1 100
2 300
2 99
3 100
5 100
5 999
>>1599

9
5 5
4 6
4 12
3 8
4 18
2 10
2 5
1 7
1 14
>>59
"""