n,m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid-1

    else:
        # 이미 최소 m은 확보하고 있는 상황임
        # 그래서 result에 우선 mid을 담아둠
        # 만약에 더 최대 높이를 확보할 수 있으면 땡큐
        # 아니면 그냥 얘를 반환하면 됨
        result = mid
        start = mid+1

print(result)