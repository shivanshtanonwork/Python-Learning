import sys
import itertools

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# itertools - iteration tools

arr = [1,5,5,7]
print(list(itertools.combinations(arr,2)))
print(list(itertools.combinations_with_replacement(arr,3)))

print(list(itertools.permutations(arr,2)))

arr1 = [1,2]
arr2 = [3,4]
print(list(itertools.product(arr1,arr2)))


arr = list(itertools.repeat(5,6))
print(arr)

print(list(itertools.chain([1,2],[5,6],[3,4])))

print(list(itertools.accumulate(arr)))

print(list(itertools.accumulate(arr,lambda x,y:x*y)))