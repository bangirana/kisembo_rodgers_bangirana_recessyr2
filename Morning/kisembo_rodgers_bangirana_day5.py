# Function

# Functions in python are defined using the 'def' keyword, followed by the function name
# Parenthesis (), inside parenthesis you put a parameter name, and a colon :

# Example 1
def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)

# Example 2: Multiple Return Values
def get_cooradinates():
    return 10,20

x,y = get_cooradinates()
print(x,y)

# Execise 1: Define a function greetings with a parameter name, set to 'Guest' 
# and print a message 'I am a software programmer'
def greetings(guest, name):
    print(f"I am {name} software programmer and I am {guest}")
    return guest, name
result = greetings('Kisembo', 'Rodgers')

# Example 3

def get_name_and_position():
    name = "Bangirana"
    position = "I am a software engineer"
    return name ,position
name, postion = get_name_and_position()
print(name, postion)

def get_name_and_age():
    name = "Rodgers"
    age = 23
    return name ,age
name, age = get_name_and_age()
print(name, age)

# Notes
"""
def : Keyword to define a function
function_name: name of function
parameter: Optinal, arguments passed to the function
Docstring: Optional, describes the function purpose
return: Optional, returns a value from the function

"""

# Syntax for defining a function
# def function_name(parameter):
#     """Docstring optional"""
#     Function body
#     return value


# Lambda function
# These are small anonymous functions defined unsing the lambda keyword.\
# They are restricted to a single expression

# Syntax for lambda function
# lambda parameter: expression

# Example 4: Create a lambda fucntion to add two numbers

add = lambda a, b : a + b
print(add(20, 63))

# Example 5: Use cases of lamba function for sorting
coordinates = [(1,2), (2,3), (3,1), (5,0)]
coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)

# Map, Filter, and Reduce
# Example 6:

number_squares = [1, 2, 3, 4, 5]
squares = list(map(lambda x : x**2, number_squares))
print(squares)

# Exercise 4: Define a function to get user info that accepts arbitrary keyword
# arguments and print each key value pair


def get_my_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

get_my_info(name = "Kisembo", age=23, course="Software Engineer", Year_of_study=3)
