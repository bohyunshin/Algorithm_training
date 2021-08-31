from collections import defaultdict
def recursive(index,a,banned_id,m,dct,default_dct=defaultdict(int),ans=defaultdict(int)):
    if index >= m:
        a.sort()
        if ans[' '.join(a)] == 0:
            ans[' '.join(a)] += 1
        return
    user_id = dct[banned_id[index]]
    for i in range(len(user_id)):
        if default_dct[user_id[i]] >= 1:
            continue
        a[index] = user_id[i]
        default_dct[user_id[i]] += 1
        recursive(index+1,a,banned_id,m,dct,default_dct,ans)
        default_dct[user_id[i]] -= 1
    return ans

def solution(user_id, banned_id):
    answer = 0
    dct = defaultdict(list)
    for b_id in banned_id:
        for u_id in user_id:
            if len(b_id) == len(u_id):
                FLAG = True
                for b,u in zip(b_id, u_id):
                    if b != '*' and b != u:
                        FLAG = False
                        break
                    elif b == u:
                        continue
                    elif b_id == '*' and b != u:
                        continue
                if FLAG == True:
                    if u_id not in dct[b_id]:
                        dct[b_id].append(u_id)
    a = ['']*(len(banned_id))
    ans = recursive(0,a,banned_id,len(banned_id),dct)
    print(ans)
    # return answer