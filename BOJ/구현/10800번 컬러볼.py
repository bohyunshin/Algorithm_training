from collections import defaultdict
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ball = []
    for i in range(n):
        c, s = map(int, sys.stdin.readline().split())
        ball.append([c, s, i])

    # 공의 크기 순으로 정렬
    ball.sort(key=lambda x: x[1])

    answer = defaultdict(int)
    ball_size_sum = defaultdict(int)  # 색깔 별 공의 크기 누적합

    total = 0  # 총합
    i, j = 0, 0
    for i in range(n):
        while ball[j][1] < ball[i][1]:  # 크기가 작을 때까지 수행
            total += ball[j][1]
            ball_size_sum[ball[j][0]] += ball[j][1]
            j += 1
        answer[ball[i][2]] = total - ball_size_sum[ball[i][0]]  # 총합 - 현재 색깔 공 누적합

    for i in range(n):
        print(answer[i])

# n = int(input())
# balls = []
# color_num = -1
# for p in range(n):
#     c,s = map(int,input().split())
#     c -= 1
#     color_num = max(color_num, c)
#     balls.append((p,c,s))
# balls.sort(key=lambda x: x[2])
# colors = [0]*(color_num+1)
# psum = [0]*(n)
# ans = []
# # 초기값 설정.
# p,c,s = balls[0]
# psum[0] = 0
# colors[c] = s
# ans.append((p,0))
# for i in range(1,n):
#     p,c,s = balls[i]
#     print(p,c,s)
#     colors[c] += s
#     psum[i] = psum[i-1] + s - colors[c]
#     ans.append((p,psum[i]))
# print(ans)
# # print(psum)
# # print(balls)