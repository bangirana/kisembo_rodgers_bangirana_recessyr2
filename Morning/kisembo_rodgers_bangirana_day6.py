# Error Handling in Python
# Exception Handling with try, except, else, and finally
# Custom exceptions

"""
The Summary

Error handling in python helps to handle unexpected situations and errors

1. Try: Contains code that might throw an exception
NB: If an exception occurs, the rest of the code in the try block is skipped or ignored

2. Except: Catches and handles exceptions
NB: You can specify different handlers for different types

3. Else: The code runs if no exception occurs
NB: If no exceptions are raised in the try block, it runs

4. Finally: It runs whether an excption is raised/occured or not
NB: Ued for cleaning up acions

"""
# Example 1: Handle exceptions with division by zero

try:
    num = int (input("Enter a number: "))
    result = 20 / num

except ValueError:
    print("Invalid number. Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("The result is: ", result)

finally:
    print("Execution completed successfully.")

# Exercise 1: Write a function that converts a string to an integer
# and handle both valueError 
# If the string cannot be converted to an interger and the TypeError if the
# the input is not a string
# Use multiple except block to handle these exceptions

def convert_to_string(myString):
    try:
        result = int(myString)
        print(f"My converted value is : {result}" )
    except ValueError:
        print("Error: The string cannot be converted to an integer.")

    except TypeError:
        print("Error: The input is not a string.")

    else:
        print("The string has been converted to an integer: ", result)

convert_to_string

myStringInput = input("Enter a string: ")
myInt = convert_to_string(myStringInput)

# Custom exception handling
# Example 2: Exceptioon raised for error in the input, if funds are insufficient

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account"
        
        super().__init__(self.message)

def withdraw(balance, amount):
    if balance < amount:
        raise InsufficientFundsError(balance, amount)
    else:
        return balance - amount

# Custom exception handling
try:
    balance = 200000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)
    # print(f"New balance: {new_balance}")

except InsufficientFundsError as e:
    print(f"Error: {e.message}")

else:
    print(f"Withdrawal successful! New balance is {new_balance}")

finally:
    print("Transaction complete. Thank you for banking with us!")

# Note: 
"""
Defining a Custom Exception
Class CustomError(Exception):
    Custom Exception for specific error cases

def __init__(sefl, message):
    super().__init__(message)
    self.message
# Raising a Custom Exception
def check_value(value):
    if value < 0 or value:
    raise CustomError("Value should be a positive integer")
return value

# Handle exception with try, except, else and finally
try:
    result = check_value(-10)

except CustomError as e:
    print(f"Error: {e.message}")

finally:
print("Transaction complete. Thank you for banking with us!")
"""

# Exercise 2: Create a custom exceptioon InvalidAgeError and a write a function that raises this 
# exception if the given age is negative. Handle this custom excepion when calling this function

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Inputting the age of {age}"
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    return age

try:
    age = int(input("Enter your age: "))
    result = check_age(age)
    # print(f"Your age is {result}")

except InvalidAgeError as e:
    print(f"Error: {e.message}")

finally:
    print("Age verification successfull!")
