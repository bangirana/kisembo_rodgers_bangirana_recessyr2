# Dictionaries
# Creating amd using dictionaries
# Dictionary methods and operations


"""
Dictionaries in pythons are collections of keys and values.
-Unordered
-Mutable
-Indexed by keys

"""

# Create a dictionary for a student pursuing software engineering,
# Key must be name, age technology interest, course and year of study
# Put your own details

context = {
    'name' : 'Kisembo Rodgers Bangirana',
    'age' : 24,
    'technology interest' : 'Ai',
    'course' : 'Software engineering',
    'Year of study' : 2,
}

print(context['age'])

# Access values
# Modify values

# Execise 1: Modify age and technology
context['age'] = 30
context['technology interest'] = "DevOps"
print(context)

# Adding keys and values
context['email'] = 'kisemborodgers100@gmail.com'
print(context)

# Exercise 2: Remove key and value
context.pop("technology interest")
print(context)

# Or
# del context("technology interest")

# Common dict methods
"""
get() - returns value for the specified key if not it returns the default value(None)

update() - updates the dictionary with the elements from another dictionary

pop() - removes the specified key and the corresponding value

"""

# Example 3 : Using get() method

print(context.get('name'))

# Exercise 3: Use the update method to change value in age
context.update({'age': 78})
print(context) 

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary and return output

if context['age'] is not None:
    print(context['age'])

# keys(), value() and the items() methods
print(context.keys())
print(context.values())
print(context.items())

"""
keys() - return a view of objects taht displays a list of all keys
values() - returns a view of values  that displays a list of all values
items() - returns a view of objects that displays a list of keys and values as tuple pairs

"""

# Exercise 5: Use the update method to change the course and add a new key 'Whatsapp_Number' 
# to the dictionary

context.update({'course' : 'BSCS', 'Whatsapp_Number': '0778898762'})
print(context)
