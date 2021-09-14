from bisect import bisect, bisect_left, bisect_right
def biary_search(array,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None
def calCountsByRange(array,left_value,right_value):
    r_i = bisect_right(array,right_value)
    l_i = bisect_left(array,left_value)
    return r_i - l_i

array = [0,1,3,4,5,5,5,5,5,6,7]
print(calCountsByRange(array,4,5))