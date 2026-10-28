# # Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"

# Call the 'greet' function
def greet():

    print('hello World!')

greet()

#question 2 

def greet(firstname,lastname):
    print("Hello " + firstname+' '+ lastname + '!')

greet('Bilqees','Moos')

# Question 3: Function with Return Value

#define the function

def square(number):
    return number * number

print(square(5))

# Question 4: Function with Multiple Parameters and Return Value
def rectangle_area(length , width) :
    return length*width
print(rectangle_area(4,5))

# Question 5: Using a Function as an Argument
def apply_operation(function , number):
    return function(number)
    
def double(number):
    return number * 2

print(apply_operation(double, 7))

      
print(apply_operation(square, 3))