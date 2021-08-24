A = list(map(int, input().split()))
idx1 = [1,3,5,7,9,11,24,22]
idx2 = [2,4,6,8,10,12,23,21]
idx3 = [13,14,5,6,17,18,21,22]
idx4 = [15,16,7,8,19,20,23,24]

c1 = [A[i-1] for i in idx1]
c2 = [A[i-1] for i in idx2]
r1 = [A[i-1] for i in idx3]
# 무슨 차이?...
# r3 = [i for index,i in enumerate(A) if index+1 in idx3]
r2 = [A[i-1] for i in idx4]

def rotate(c1,c2,r1,r2,which,vertical,direction):
    if vertical == True and which == 'first':
        if direction == 'clock':
            c1 = c1[-2:] + c1[:-2]
        else:
            c1 = c1[2:] + c1[:2]
        r1[2] = c1[2]
        r1[-1] = c1[-1]
        r2[2] = c1[3]
        r2[-1] = c1[-2]
        return c1,c2,r1,r2
    if vertical == True and which == 'second':
        if direction == 'clock':
            c2 = c2[-2:] + c2[:-2]
        else:
            c2 = c2[2:] + c2[:2]
        r1[3] = c2[2]
        r1[-2] = c2[-1]
        r2[3] = c2[3]
        r2[-2] = c2[-2]
        return c1, c2, r1, r2
    if vertical == False and which == 'first':
        if direction == 'clock':
            r1 = r1[-2:] + r1[:-2]
        else:
            r1 = r1[2:] + r1[:2]
        c1[2] = r1[2]
        c1[-1] = r1[-1]
        c2[2] = r1[3]
        c2[-1] = r1[-2]
        return c1, c2, r1, r2
    if vertical == False and which == 'second':
        if direction == 'clock':
            r2 = r2[-2:] + r2[:-2]
        else:
            r2 = r2[2:] + r2[:2]
        c1[3] = r2[2]
        c1[-2] = r2[-1]
        c2[3] = r2[3]
        c2[-2] = r2[-2]
        return c1, c2, r1, r2

def check(c1,c2,r1,r2):
    index = [0,2,4,6]
    for i in range(len(c1)):
        if i in index:
            if (c1[i] == c2[i] == c1[i+1] == c2[i+1]) is False:
                return False
            if (r1[i] == r2[i] == r1[i+1] == r2[i+1]) is False:
                return False
    return True

which = ['first','second']
vertical = [True, False]
direction = ['clock','unclock']
for d in which:
    for v in vertical:
        for c in direction:
            nc1,nc2,nr1,nr2 = rotate(c1,c2,r1,r2,d,v,c)
            if check(nc1,nc2,nr1,nr2) == True:
                print(1)
                exit()
print(0)