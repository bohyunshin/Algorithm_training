n,m = map(int, input().split())
numbers = [i for i in range(1,n+1)]
# a = []
# def solution(index,a,m):
#     if len(a) == m:
#         print(' '.join(list(map(str,a))))
#         return
#     if index >= len(numbers):
#         return
#     solution(index+1,a+[numbers[index]],m)
#     solution(index+1,a,m)
# solution(0,a,m)

a = [0]*m
def solution(index, selected,n,m):
    if selected == m:
        print(' '.join(list(map(str,a))))
        return
    if index > len(numbers):
        return
    a[selected] = index
    solution(index+1, selected+1, n, m)
    a[selected] = 0
    solution(index+1, selected, n, m)
solution(1,0,n,m)