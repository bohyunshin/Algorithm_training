from string import ascii_lowercase
n,k = map(int, input().split())
words = []
for _ in range(n):
    words.append(input())
lang = ['a','c','i','n','t']
if k < len(lang):
    print(0)
    exit()
if k == len(lang):
    answer = 0
    for word in words:
        temp = 0
        for alpha in word:
            if alpha in lang:
                temp += 1
        if temp == len(word):
            answer += 1
    print(answer)
    exit()
lang_bit = [index for index,alpha in enumerate(ascii_lowercase) if alpha in lang]
myhash = {}
for index, alpha in enumerate(ascii_lowercase):
    myhash[alpha] = index
answer = -1
# 나머지 21개 알파벳에 대해서만 비트마스킹 진행하면 됨.
for s in range(1<<21):
    temp = 0
    for b in range(21):
        if s & (1 << b) > 0:
            temp += 1
    if temp != k-len(lang):
        continue
    word_read = 0
    for word in words:
        temp = 0
        for alpha in word[4:(len(word)-4)]:
            b = myhash[alpha]
            if s & (1 << b) > 0:
                temp += 1
        if temp == len(word)-8:
            word_read += 1
    answer = max(answer, word_read)
    # print(word_read)
print(answer)
