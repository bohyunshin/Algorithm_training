n = int(input())
box = list( map(int, input().split()) )
# dp 테이블 정의
# dp[i]: box의 i번째 원소까지 고려할 때 넣을 수 있는 최대 상자 수
dp = [1]*n
# 최소 자기 자신을 포함할 수 있으므로 기본 값은 모두 1
dp[1] = 1
for i in range(1,n):
    for j in range(i):
        # i번째 상자의 크기가 j번째 상자보다 크다면 j번째 상자를 넣을 수 있음
        # 다만, 관심있는 것은 최대값이니까 이전 값보다 클때만 업데이트 함
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))