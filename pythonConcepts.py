# Task 1
name = "Luke"
age = 21
height = 71.5
print(f"My name is {name}, I am {age} years old and {height} inches tall.")

# Task 2
num1 = 20
num2 = 4

print("The sum of 20 and 4 is", num1 + num2) # + op for addition
print("The difference between 20 and 4 is", num1 - num2) # - op for subtraction
print("The product of 20 and 4 is", num1 * num2) # * op for multiplication
print("The quotient of 20 and 4 is", num1 / num2) # / op for division

# Task 3
num = int(input("Enter a number: ")) # wrap using int() to convert input to int

if num > 0:
 print("This number is positive. Awesome!")
elif num < 0:
 print("This number is negative. Better luck next time!")
else:
 print("Zero it is. A perfect balance!")