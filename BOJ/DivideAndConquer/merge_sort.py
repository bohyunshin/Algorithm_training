a = [5,3,2,9,7,4,1]
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
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
            k += 1
        else:
            b[k] = a[j]
            j += 1
            k += 1
    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= end:
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(start,end+1):
        a[i] = b[i-start]
    return
sort(0,len(a)-1)
print(a)