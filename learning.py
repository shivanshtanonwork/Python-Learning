import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

arr = [1,6,2,4]
arr.append(7)
print(arr)

arr.extend([1,4])
print(arr)

arr.insert(2, 15)
print(arr)

arr.remove(4)
print(arr)

arr.pop()
print(arr)

print(arr.index(7))
print(arr.count(1))

arr.sort()
print(arr)

arr.reverse()
print(arr)

# arr.clear()
# print(arr)

arr2 = arr.copy()
print(arr2)
arr2[0] = 1999
print(arr2)