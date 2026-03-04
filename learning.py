import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# string methods

name = "   Shivansh tandon.  "
# none of the methods impacts or changes the original string
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

print(name.strip())

print(name.split())
print(name.split('a'))

arr = ["Shivansh", "Tandon"]
print("-".join(arr))

 
print(name.replace("Shivansh", "Shiva"))

print(name.find("tandon"))

print(name.index("Shivansh"))

print(name.startswith("h"))
print(name.endswith(' '))

print(name.count("n"))
print(name.isalpha()) #False cause it has spaces 

