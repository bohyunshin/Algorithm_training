def go(x,W,ans):
    if len(W) == 2:
        ans.append(x)
        return
    n = len(W)
    for i in range(1,n-1):
        go(x+W[i-1]*W[i+1],[j for index,j in enumerate(W) if index != i],ans)
    return ans
def solution(n,W):
    ans = go(0,W,[])
    return ans
if __name__ == '__main__':
    n = int(input())
    W = list(map(int, input().split()))
    ans = solution(n,W)
    print(max(ans))