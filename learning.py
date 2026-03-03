import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

arr = [5,6,1]
print(list(reversed(arr)))

arr = list(range(1,5))
print(arr)