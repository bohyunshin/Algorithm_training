MAX = 1000000
check = [False]*(MAX+1)
check[0] = check[1] = True
prime = []
for i in range(2, MAX+1):
    if i % 2 == 0:
        check[i] = True
        continue
    if check[i] is False:
        prime.append(i)
        j = i*i
        while j <= MAX:
            check[j] = True
            j += i

while True:
    n = int(input())
    if n == 0:
        break
    conjecture = False
    for a in prime:
        b = n-a
        if check[b] == False:
            print(n, '=', a, '+', b)
            conjecture = True
            break

    if conjecture == False:
        print("Goldbach's conjecture is wrong.")