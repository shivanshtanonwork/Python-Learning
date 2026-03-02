import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# String Methods
name = "tAndon"
print(name.capitalize()) # it doesn't changes the string 
print(name.upper())
print(name.lower())
print(name.find("don"))