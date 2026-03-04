import sys
import random

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# random modules
print(random.random())

print(random.randint(1,6))

print(random.randrange(0,10,2))

print(random.choice([1,6,8,9]))

print(random.sample([1,6,8,9],2))

arr = [1,5,6,7]
random.shuffle(arr)
print(arr)

print(random.uniform(1.0, 9.0))