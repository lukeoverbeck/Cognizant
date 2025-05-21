# Task 1

while True:
 try:
  n = int(input("Enter a number, which be divided in the form 100 / (your number): "))
  print(f"Result: {100/n}")
  break
 except ZeroDivisionError:
  print("Oops! You cannot divide by zero.")
 except ValueError:
  print("Invalid input! Please enter a valid number.")

# Task 2

# The error occurs when the index is out of the bounds of the list. I handled it by raising an IndexError in the function
def list_index(n, list):
 if n > len(list) - 1 or n < 0:
  raise IndexError("Index error occurred! List index out of range.")
 print(f"Num at index {n}: {list[n]}")
while True:
 try:
  n = int(input("Enter an index of the list, 0-4, to print out the number at this index: "))
  list = [1, 2, 3, 4, 5]
  list_index(n, list)
  break
 except IndexError as e:
  print(e)
 except ValueError:
  print("Invalid input! Please enter a valid number.")

print()

# The error occurs when the user input a key not found in the dictionary. I handled it by raising a KeyError in the function
def dictionary_key(key, dictionary):
 if key not in dictionary.keys():
  raise KeyError("KeyError occurred! Key not found in dictionary.")
 print(f"Value at {key}: {dictionary[key]}")
while True:
 try:
  key = input("Enter a key in the dictionary to print out the value: ")
  dictionary = {
   "name": "Luke",
   "car": "Lexus",
   "color": "blue",
   "year": 2004
  }
  dictionary_key(key, dictionary)
  break
 except KeyError as e:
  print(e)

print()

# The error occurs because one of the variable is a string, and the other is an int.
# In this case, I did not ask for input from the user, but passed hardcoded parameters to the function.
# I handled the error by raising a TypeError in the function
def addition(a, b):
 if type(a) == str and type(b) == int or type(a) == int and type(b) == str:
  raise TypeError("TypeError occurred! Unsupported operand types.")
 print(f"{a} + {b} = {a+b}")
try:
 print("Now, we will try and add 'yes' and 5:", end=" ")
 addition("yes", 5)
 
except TypeError as e:
 print(e)

print()

# Task 3
# Only breaks the while loop if the else condition is reached, indicating successful division
while True:
 try:
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))
  result = a/b
 except ZeroDivisionError:
  print("Oops! You cannot divide by zero.")
 except ValueError:
  print("Invalid input! Please enter a valid number.")
 else:
  print(f"The result is {result}")
  break
 finally:
  print("This block always executes.")
