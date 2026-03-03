import sys
import math

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

arr = [-15, 6,8,7]
print(max(arr, key=lambda x: abs(x)))

fruits_list = ["kiwi", "apple","pineapple"]
print(max(fruits_list,key=len))

print(sum(arr))
print(math.prod(arr)) 

arr1 = [True,False,True]
print(any(arr1))
print(all(arr1))

def count_element(arr2, number):
    count = 0
    for i in arr2:
        if i == number:
            count+=1
    return count

arr2 = [1,2,1,7]
print(count_element(arr2,1))