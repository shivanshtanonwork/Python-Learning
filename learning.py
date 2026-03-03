import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# (key, value)

from collections import defaultdict

dd = defaultdict(int)
dd[1] ="shivansh"
print(dd[1])
dd["fname"] = "shivansh"
dd['u'] = 99
dd['list'] = [1,2,4]
print(dd['list'])
print(dd["xyz"]) # since it's a defaultdict initialised with int it always returns 0