l,c = map(int, input().split())
s = input().split()
s.sort()

def check(password):
    ja = 0
    mo = 0
    for s in password:
        if s in ['a','e','i','o','u']:
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1

def go(n,alpha,password,i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i >= len(alpha):
        return
    go(n,alpha,password+alpha[i],i+1)
    go(n,alpha,password,i+1)

go(l,s,"",0)

# def solution(s,s_others,count,ja,mo):
#     print(s)
#     if count == l and ja >= 2 and mo >= 1:
#         return ' '.join(s)
#     if count == l and (ja < 2 or mo < 1):
#         return ""
#     answer = []
#     for i in s_others:
#         temp = [i for i in s_others if i not in [i] + s]
#         if i in ['a','e','i','o','i']:
#             answer.append(solution(s+[i],temp,count+1,ja,mo+1))
#         else:
#             answer.append(solution(s + [i], temp, count + 1, ja+1, mo))
#     return answer
# result = solution([],s,0,0,0)
# print(result)