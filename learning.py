import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# dict methods

dd = {1: "Shivansh" ,2: "Shiva", 3:"Shiv"}

dd[100] = "Century"
dd.update({10:"Messi"})
print(dd)

print(dd.get(1))

print(dd.get(11,"not found"))

print(dd.pop(100))
print(dd)

dd.popitem()
print(dd)

arr = list(dd.keys())
print(arr)
arr = list(dd.values())
print(arr)
arr = list(dd.items())
print(arr)

for item in dd.items():
    print(item[0],item[1])