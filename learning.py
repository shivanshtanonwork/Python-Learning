import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# Type Conversion
x = int(input())
y = int(input())
num = x+y
print(num)

# int()
# float()
# str()
# bool()

# comparing operators
num1 = 10
num2 = 12


print(num1 == num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)