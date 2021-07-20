n = int(input())
box = list( map(int, input().split()) )

# result 리스트에는 (포개진 상자의 개수, 포개진 상자 중 가장 큰 사이즈)가 담겨져 있음
result = [ (1,box[0]) ]

# 두번째 상자부터 살펴봄
for b in box[1:]:
    to_add = []
    for tup in result:
        # 살펴본 상자의 크기가 더 크다면 상자를 포갤 수 있음
        if tup[-1] < b:
            # 형식은 (포개진 상자의 개수, 살펴본 상자의 크기)
            to_add.append( (tup[0]+1, b) )
    result += to_add
answer = 0
# print(result)
for i in result:
    if answer < i[0]:
        answer = i[0]
print(answer)