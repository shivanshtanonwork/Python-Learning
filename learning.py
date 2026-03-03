import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# lists
nums = [1,5,6,7,7,9]
print(len(nums))

for items in nums:
    print(items)

nums.append(10)
print(nums)
nums.clear()
print(nums)
