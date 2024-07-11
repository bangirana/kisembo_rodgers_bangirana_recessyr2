# Inheritance and Polymorphism

"""_summary_

Inheritance and method overriding
Polymorphism and method resolution
order
Abstract classes and interfaces

    """

# Inheritance and method overriding
"""_summary_
--description
Inheritance and method overriding allows a class(child class) to inherit attributes and methods
from another class (parent class).

Key concepts
Base class (parent class): Class whose properties are inherited by another class.
Derived class (child class): Class that inherits attributes and properties from another base class.

    """

# Example 1: Syntax Create a class where a dog inherits from animal and overrides with a speak method

print("Example 1")


class Animal:
    def speak(self):
        return "Woof woof woof woof"


class Dog(Animal):
    def speak(self):
        return "Barks"


# Implementatiion of inherited classes

animal = Animal()
dog = Dog()

print(animal.speak())
print(dog.speak())

# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Method resolution Order (MRO). is order in which python looks for a method in hierarchy classes.

# Example 2: How polymorphismworks in python

print()
print("Example 2")


class Animal:
    def speak(self):
        return "Quack Quack"


class Dog(Animal):
    def speak(self):
        return "Barks"


class Cat(Animal):
    def speak(self):
        return "Meow"


def make_animal_speak(animal):
    print(animal.speak())


make_animal_speak(Dog())
make_animal_speak(Cat())


# Exercise 1: Create a simple application to manage different types of vehicles. Implement
# derived class to demonstrate inheritance and polymorphism.
"""
Requirements
1. Base class to vehicle
Attributes: make, model and year
Methods: display_info()

2. Derived classes:
Car: inherits from vehicle
attributes: number_of_doors,
Overrides: display info()

Motorcycle: inherit from vehicle
Attributes: type_of_bike (cruiser, sport, touring)
Overrides: display_info()

# Exercise 2:
Create a function that accepts a list of vehicle objects and call their display_info() method
to print details of each vehicle.
"""
print()
print("Exercise 1 solution")

# Exercise 1 solution


class Vehicle:
    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Vehicle details - Make: {self.make}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):

    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        return f"Car details - Make: {self.make}, Model: {self.model}, Year: {self.year}, Number of Doors: {self.number_of_doors}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def display_info(self):
        return f"Motorcycle details - Make: {self.make}, Model: {self.model}, Year: {self.year}, Type of Bike: {self.bike_type}"


def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())


car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Yamaha", "MT-07", 2021, "Sport")

vehicles = [car, motorcycle]
display_vehicle_info(vehicles)

print()


# Reading and Writing Files

"""_summary_
Working with text files
Handling CSV files
JSON and XML file processing

 """
# 1. Working with text files, open, read, write and close
# Note: python provides inbuilt functions to handle text files.
# Key concepts
"""_summary_

Opening File: open() function (r, w, a, r+)
Reading File: read() function
Writing File: write() function
Close File: close() function



"""

# Example 3: write a file and read a file
print("Example 3")

# Writing to a text file
with open("kisembo.txt", "w") as file:
    file.write("I am Kisembo and i love python.\n")
    file.write("I use python for automation")

# Reading from a text file
with open("kisembo.txt", "r") as file:
    content = file.read()
    print(content)

# Handling CSV files
"""
CSV ( Comma Separated Values) file used widely for data exchange. you can read a file but cannot write to the file hence safeguards the integrity of data

Key Concepts:
Reading CSV files: Using 'csv.reader'
Writing CSV files: Using 'csv.writer'
DictReader and DictWriter: The class read and write files as dictionaries.


"""
print()
print("Example 4")
# Example 4: Writing and Reading CSV files

import csv

# Writing to a CSV file
with open("kisembo.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "position", "course"])
    writer.writerow(["kisembo rodgers", "Student", "BSE"])
    writer.writerow(["Sserungogdi", "Student", "BSE"])
    writer.writerow(["Mukisa", "Student", "BSE"])

# Reading from a CSV file
with open("kisembo.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# JSON and XML file processing
"""summary_line

JSON ( Javascript Object Notation ) and XML ( extensible Markup Language ) are formats used to
structure data.
Key Concepts 
Loading JSON data: using json.load() for reading JSON file 
Dumping JSON Data: using json.dump() for writing JSON file
Parsing JSON Fata: using json.loads() for handling JSON strings


"""

# Example 5: Write and read JSON file
print()
print("Example 5")

import json

# writing to a JSON file

student_data = {"name": "kisembo", "course": "BSE", "year": "Year2"}

# Open the file
with open("student_data.json", "w") as json_file:
    json.dump(student_data, json_file)


# Reading the JSON file
with open("student_data.json", "r") as json_file:
    student_data = json.load(json_file)
    print(student_data)

# Exercise 2: Write and read the xml file.
print()
""" how to write to an xml file

1. Create the root element of the XML document that will contain all other elements.
root = ET.Element("root")

2. Create Sub-elements and Populate Data
Add child elements (sub-elements) to the root element 
student = ET.SubElement(root, "Student")

3. Create an ElementTree Object
Create an ElementTree object from the root element. This object represents the entire XML document.
tree = ET.ElementTree(root)

4.  Write the XML to a File usin 'wb' """


print("Exercise 2 Solution")

# Writing to xml file
import xml.etree.ElementTree as ET


student_details = {
    "Student": {"name": "kisembo rodgers", "age": "25", "course": "BSE", "address": "Paris"}
}


root = ET.Element("root")

student = ET.SubElement(root, "Student")
for key, value in student_details["Student"].items():
    child = ET.SubElement(student, key)
    child.text = value


tree = ET.ElementTree(root) 

# Writing the tree to an XML file
with open("student_details.xml", "wb") as files:
    tree.write(files)

print("XML file written successfully.")

# Reading the XML file
tree = ET.parse("student_details.xml")
root = tree.getroot()

# print data
for student in root.findall("student"):
    name = student.find("name").text
    age = student.find("age").text
    course = student.find("course").text
    address = student.find("address").text
    print(f"Name: {name}, Age: {age}, Course: {course}, Address:{address}")


# Exercise 3: Using abstraction calculate the area and perimeter of a rectangle.
""" 
Abstraction is used to hide implementation details

Abstract Class: A class that cannot be 
instantiated on its own and is meant to be subclassed.


Abstract classes can have one or more abstract methods. 
These methods do not have a body; they only have a signature.

Abstract Method: A method declared in an abstract class without an implementation.
Subclasses are required to provide an implementation for these methods.


"""
print()
print("Exercise 3 Solution")

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Creating a Rectangle object
rect = Rectangle(10, 5)

# Calculating area and perimeter
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
