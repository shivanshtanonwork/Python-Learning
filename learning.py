import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

from collections import Counter

arr = Counter([1,2,2,3,2,3,3,4]) # Count elements 
print(arr)
print(arr[2])

print(arr.most_common(2)) # 2 here is top 2

print(list(arr.elements())) # python follows the insertion order

arr.update([7])
arr.subtract([3])
print(list(arr.elements())) 
