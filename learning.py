import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# ternary operator
age = int(input())
status = "Adult" if age >= 18 else "Minor"
print(status)

# comparison operators and or 
x = 10
y = 15
z = 5

if x > y and x > z:
    print(f"{x} is greatest")
elif y > x and y > z:
    print(f"{y} is greatest")
elif z > x and z > y:
    print(f"{z} is greatest")
else:
    print("They may be equal nos.")


name = input()
if len(name)>0 and (name[1] == "S" or name[-2] == "h"):
    print("yes")
else:
    print("no")