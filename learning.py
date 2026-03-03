import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

from collections import deque
# deque - (double-ended queue)
dq = deque([2,3,1])

dq.append(5) # adds element from right or end
print(dq)

dq.appendleft(15)
print(dq)

dq.pop() # pops out last element from right 
print(dq)

dq.extend([10,"Shivansh"])
print(dq)

dq.extendleft([1999,27])
print(dq)