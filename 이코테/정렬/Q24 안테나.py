n = int(input())
antena = list(map(int, input().split()))
antena.sort()
if len(antena) % 2 == 0:
    index = len(antena) // 2 - 1
else:
    index = len(antena) // 2
print(antena[index])