import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

for i in range(0,15):
    print("Hello Shivansh")


for i in range(0,10,2):
    print(i)

for i in range(15, 0, -1):
    print(i)

for i in range(0,5):
    print(f"value of i {i}")
    print()
    for j in range(0,5):
        print(f"value of j {j}")
    print()

i = 0
while i < 5:
    print(i)
    i = i + 1   


for i in range(0,5):
    print("Hello")
    if i == 3:
        break
else:
    print("Entire loop was run")