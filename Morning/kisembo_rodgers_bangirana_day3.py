# Day 3 Morning Session code
# List Comprehension

list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)

# Exercise 1
# Create a list of even squares of range 20

even_squares = [i**2 for i in range(20) if i**2 % 2 ==0]
print(my_even_squares)


#Dictionary Comprehension
favorite_cars = ['BMW', 'Mercedes', 'FordRaptor']
car_length = {car: len(car) for car in favorite_cars}
print(car_length)


#Exercise 2
# Create a list of tuple where each tuple contains a number and its cube for numbers between 1 and 10 using
# dictionary comprehension

cube_list = {i: i**3 for i in range(1,11)}
print(cube_list)



