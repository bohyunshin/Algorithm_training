import heapq
n = int(input())
array = []
for _ in range(n):
    deadline, cupNoodle = map(int, input().split())
    array.append((deadline, cupNoodle))

array.sort()

queue = []

for i in array:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)

print(sum(queue))

# REF: https://velog.io/@ju_h2/Python-백준-1781.-컵라면-풀이-파이썬-탐욕-알고리즘그리디-구현-6