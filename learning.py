import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

from collections import OrderedDict

od = OrderedDict([(1,"Shivansh"),(3,"Mom"),(2,"Papa"),(4,"Vidushi"),(5,"DaduDadi")]) #typically key and value are of same data types in OrderedDict

print(od)
print(od[1])

if 5 in od:
    print(od[5])
else:
    print("Not in the dict")

od[10] = "messi"
print(od)
od.move_to_end(2, last=False)
print(od)

od.popitem()
print(od)

if 10 in od:
    print(od.pop(10))
print(od)
