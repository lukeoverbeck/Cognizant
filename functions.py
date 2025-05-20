# Task 1

def greet_user(name):
 print(f"Hello, {name}! Welcome aboard.", end=" ")

def add_numbers(a, b):
 return a + b

name = "Alice"
a = 5
b = 10

greet_user(name)
print(f"The sum of {a} and {b} is {add_numbers(a, b)}.")

# Task 2

def describe_pet(pet_name, animal_type):
 print(f"I have a {animal_type} named {pet_name}.", end=" ")

name = "Buddy"
type = "dog"
name1 = "Whiskers"
type1 = "cat"

describe_pet(name, type), describe_pet(name1, type1)
print()

# Task 3

def make_sandwich(*args):
 print("Making a sandwich with the following ingredients: ", end="")
 for item in args:
  print(f"- {item}", end=" ")

make_sandwich("Lettuce", "Tomato", "Cheese")
print()

# Task 4

def factorial(n):
 if n == 1:
  return 1
 else:
  return n * factorial(n - 1)

def fibonacci(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  return fibonacci(n - 1) + fibonacci(n - 2)
 
n = 5
num = 6
print(f"Factorial of {n} is {factorial(n)}. The {num}th Fibonacci number is {fibonacci(num)}.")