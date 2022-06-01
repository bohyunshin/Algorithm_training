n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
l = x+y
def sort(start,end):
    if start == end:
        return
    mid = (start+end) // 2
    sort(start,mid)
    sort(mid+1,end)
    merge(start,end)
def merge(start,end):
    mid = (start+end) // 2
    i = start
    j = mid+1
    k = 0
    b = [0]*(end-start+1)
    while i <= mid and j <= end:
        if l[i] < l[j]:
            b[k] = l[i]
            i += 1
            k += 1
        else:
            b[k] = l[j]
            j += 1
            k += 1
    while i <= mid:
        b[k] = l[i]
        i += 1
        k += 1
    while j <= end:
        b[k] = l[j]
        j += 1
        k += 1
    for i in range(start,end+1):
        l[i] = b[i-start]
    return
sort(0,len(l)-1)
print(' '.join(map(str,l)))
