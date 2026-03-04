import sys
import heapq

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

val = []
heapq.heappush(val,10)
heapq.heappush(val,7)
heapq.heappush(val,15)
heapq.heappush(val,7)
heapq.heappush(val,2)  # it always gives us the 1st element as minimum element
print(val)

heapq.heappop(val) # smallest element is popped out
print(val)

print(heapq.heappushpop(val,4))  # 1st smaller one pushes in and then pops out
print(val)

print(heapq.heapreplace(val,3))
print(val)


print(heapq.nlargest(3, [7, 1, 5, 3, 10])) # in this iterable give me 3 largest element


arr = [7,8,10,1,-15,2]
heapq.heapify(arr)
print(arr)

# max heap
arr = [6, 7, 8, 10, 9]
pq = []
for item in arr:
    heapq.heappush(pq, -1 * item)
print(-1*pq[0])