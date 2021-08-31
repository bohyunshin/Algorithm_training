k = int(input())
MAX = 1000000
sizes = []
i = 0
while 2**i < MAX:
    sizes.append(2**i)
    i+=1
# 마지막 원소 하나만 더 추가해줌.
sizes.append(2**i)
if k in sizes:
    print(k,0)
    exit()
for size in sizes:
    if size > k:
        choco_size = size
        min_size = size
        break
times = 0
eaten = 0
while eaten != k:
    # 초콜릿 쪼개기
    choco_size = choco_size // 2
    times += 1
    if eaten + choco_size > k:
        continue
    else:
        eaten += choco_size
print(min_size,times)