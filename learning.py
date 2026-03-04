import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# Set methods
# set doesn't allow to store duplicates like list

st = {1, 5, 3, 1}
print(st) # it stores everything in a sorted manner

st.add(0)
print(st)

st.remove(3)
print(st)

st.discard(15)
print(st)

st.pop() # it always pops out the 1st element from the set
print(st)

