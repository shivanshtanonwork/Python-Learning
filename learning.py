import sys
import bisect

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

arr = [5,1,6,1,7,10]
# print(arr.index(6))
def linear_search(arr,val):
    for i in range(0, len(arr)):
        if arr[i] == i:
            return i
    return -1

print(linear_search(arr,1))

# bisect binary search

a = [4,5,5,6,7,7,9,10,12,12,13]  # array must be sorted
# a.sort() #use this if array not sorted

print(bisect.bisect_left(a,5)) # bisect_left tell us left most position where the the 5 is to be inserted assuming array is sorted.

print(bisect.bisect_right(a,5)) # right most 

bisect.insort(a,5)
print(a)

# we use it binary search , sorted list
