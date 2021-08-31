def go(x,A,index,plus,minus,multiple,divide,n,ans):
    if index >= n:
        ans.append(x)
        return
    if plus >= 1:
        go(x+A[index],A,index+1,plus-1,minus,multiple,divide,n,ans)
    if minus >= 1:
        go(x-A[index],A,index+1, plus, minus-1, multiple, divide, n,ans)
    if multiple >= 1:
        go(x*A[index],A,index+1, plus, minus, multiple-1, divide, n,ans)
    if divide >= 1:
        if x < 0:
            go( -(abs(x)//A[index]), A, index+1, plus, minus, multiple, divide-1, n,ans)
        else:
            go(x//A[index], A, index+1, plus, minus, multiple, divide-1, n,ans)
    return ans

def solution(n,A,op):

    ans = go(A[0],A,1,op[0],op[1],op[2],op[3],n,[])
    print(max(ans))
    print(min(ans))

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    op = list(map(int, input().split()))
    solution(n,A,op)