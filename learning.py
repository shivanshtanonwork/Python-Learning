import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# Strings
name = "Shivansh"
name = 'Shivansh'
# name = """Shivansh"""

detail = "Shiv's age is 26"
desc = 'He is also knowm as "Shiva"'
print(detail + desc)

first_name = "Shivansh"
last_name = "Tandon"

#concatenation
full_name = first_name + " " + last_name + ' '
print(3 * full_name) # repetition

# length of string
print(len(first_name))

# indexing
# we can change entire string if we want but we cannot change letter in the string 
name = "Tandon"
# name[2] = "r" # not allowed immutable
print(name)
print(name[3:])

# Escape Sequences in python
# new line
description = "Hi I'm Shivansh Tandon \nI'm a FullStack Python AI Engineer"
print(description)
# tab space
description = "Hi I'm Shivansh Tandon \tI'm a FullStack Python AI Engineer"
print(description)

# single backlash by giving \\
description = "Hi I'm Shivansh Tandon \\I'm a FullStack Python AI Engineer"
print(description)

# Formatted Strings
naam = "Shivansh"
age = 26
role = "AI FullStack Engineer"

print(f"My name is {naam}, age is {age} and role is {role}")