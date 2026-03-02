import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# conditonal statements
num1 = 15
num2 = 10

if num1 < num2:
    print("num1 is smaller")
else:
    print("num2 is smaller")

print("End of program")

age = int(input())

if age >= 18:
    print("Adult")
else:
    print("Minor")


# if elif elif else
marks = int(input())
if marks>=90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade F")