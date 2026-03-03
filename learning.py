import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

def length(str):
    count = 0 
    for i in str:
        count = count + 1
    return count

name = "Shivansh"
print(length(name))

arr = [1,5,6,7,4]
# print(sorted(arr))
print(sorted(arr,reverse=True)) # only returns new array

# to change array 
arr.sort()
print(arr)

# sort these values according to absolute values of x - it does'nt alters the array
arr1 = [-1,5,-6,7,4]
print(sorted(arr1, key = lambda x: abs(x)))
print(arr1)

fruits_list = ["apple", "pineapple","kiwi"]
print(sorted(fruits_list, key=len))
print(sorted(fruits_list,reverse=True, key=len))