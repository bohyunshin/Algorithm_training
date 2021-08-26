n,b,c = map(int, input().split())
# 아직 사지 않은 라면의 수.
A = list(map(int, input().split()))
# B원에 산 라면의 수.
x = [0]*n
# B+C원에 산 라면의 수.
y = [0]*n
ans = 0
if b <= c:
    for i in range(n):
        ans += A[i]*b
else:
    for i in range(n):
        # 우선 B원에 사기.
        ans += A[i]*b
        # B원에 샀으니까 x 배열에 추가해주기.
        x[i] = A[i]
        # 몽땅 다 샀으니까 A 배열은 깨끗하게.
        A[i] = 0
        # 그리디하게 살펴보자.
        if i+1 < n:
            # B+C원으로 살 구석이 있는지 살펴보는 것임.
            # t1 = 0이면 (->A[I+1]=0이라면) 뒤에 아무 영향도 미치지 않음!.
            t1 = min(x[i], A[i+1])
            # B+C원에 사야하니까 B원에 산 애들은 빼줌.
            x[i] -= t1
            # B+C원에 산 애들을 더해줌.
            y[i] += t1
            # ans에는 이미 B원에 산 애들은 더해져 있음.
            # 그래서 B+C에서 C만 더해주는 것임.
            ans += t1*c
            # t1만큼 산거니까 A배열에서 빼줘야 함.
            A[i+1] -= t1
        if 1 <= i < n-1:
            # 만약 t2 >= 1이면 B+2C에 살 만한 애가 있다는 것임.
            t2 = min(y[i-1],A[i+1])
            ans += t2*c
            A[i+1] -= t2
print(ans)