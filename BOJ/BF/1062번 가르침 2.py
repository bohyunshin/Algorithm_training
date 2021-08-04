from string import ascii_lowercase
n,k = map(int, input().split())
lang = [i for i in ascii_lowercase if i not in ['a','c','i','n','t']]
myhash = {}
for index, l in enumerate(lang):
    myhash[l] = index

words = [0]*n
for i in range(n):
    s = input()
    for x in s:
        if x not in ['a','c','i','n','t']:
            words[i] |= (1 << myhash[x])
if k < 5:
    print(0)
    exit()
if k == 5:
    answer = 0
    for word in words:
        # 파이썬은 정수형이 32bit이기 때문에
        # 그냥 ~ 쓰면 앞에 자리가 모두 1로 채워진다고 함.
        # 이를 방지하기 위해서 21자리용 ~ 연산을 따로 만듦
        # (1<<21)-1은 모든 자리수가 1로 채워진 애니까 여기서 비트 b를 빼면
        # ~b한 것과 동일한 효과임.
        # 여기서는 k=5이고, 더이상 사용할 수 있는 비트가 없으므로 0을 빼줬음.
        if word & ((1<<21)-1-0) == 0:
            answer += 1
    print(answer)
    exit()

answer = -1
# 나머지 21개 알파벳에 대해서만 비트마스킹 진행하면 됨.
for s in range(1<<21):
    temp = 0
    # 필수 알파벳 5개 제외하면 가르칠 수 있는 알파벳 수는 k-5
    # 현재 비트의 1에 해당하는 자리수가 k-5개일때만 진행함.
    for b in range(21):
        if s & (1 << b) > 0:
            temp += 1
    if temp != k-5:
        continue
    word_read = 0
    for word in words:
        if word & ((1 << 21) - 1 - s) == 0:
            word_read += 1
    answer = max(answer, word_read)
    # print(word_read)
print(answer)
