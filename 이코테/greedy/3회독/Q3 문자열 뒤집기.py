s = [int(i) for i in input()]

count0 = 0
count1 = 0
before = s[0]

if before == 0:
    count1 += 1
else:
    count0 += 1

for i in range(1,len(s)):
    next_ = s[i]
    if before == next_:
        continue
    else:
        if next_ == 0:
            count0 += 1
        else:
            count1 += 1
        before = next_
print(min(count0, count1))