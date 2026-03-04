import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

val = (1,4,5) #tuples - tuples are ordered and immutable
print(val)
val1 = (4,(6,7,9))
print(val1[1][2])
a,(b,c,d) = val1
print(a,b,c,d)

from collections import namedtuple

Point = namedtuple("Point",['first', 'second'])
val1 = Point(7,9)
print(val1)
print(val1.first, val1.second)
NestedPoints = namedtuple('NestedPoints',['first', 'second'])
val2 = NestedPoints(2,val1)
print(val2)

class Pair:
    def __init__(self,first,second):
        self.first=first
        self.second=second

val = Pair(2,9)
val.first=10
print(val.first,val.second)