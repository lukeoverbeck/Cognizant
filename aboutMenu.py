import turtle

# Calculates the factorial of the function and returns the result
def factorial(n):
 if n == 1:
  return 1
 else:
  return n * factorial(n - 1)

# Calculates the nth Fibonacci number and returns the result
def fibonacci(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  return fibonacci(n - 1) + fibonacci(n - 2)

# n is always 101 at the start, this is not an argument from input by the user.
# Outputs a square spiral, moving forward a length decrementing by 1 and turning 90 degrees right after each call
# Note that this function is an example of a problem that would work better using iteration, because it does not
# shrink the problem size in a way that iteration cannot
def spiral(pen, n):
 if n == 0:
   return
 else:
  pen.forward(n)
  pen.right(90)
  spiral(pen, n - 1)

x = 1
while x == 1:
  num = int(input("Main menu:\n" \
  "1. Calculate the factorial of a number.\n" \
  "2. Find the nth Fibonacci number.\n" \
  "3. Draw a recursive spiral pattern.\n" \
  "4. Exit\n"))

  if num == 1:
    try:
     n = int(input("Enter a number to find its factorial: "))
     if (n >= 0):
      print(f"The factorial of {n} is {factorial(n)}.")
     else:
      print("Please enter an integer greater than or equal to 0.")

    except:
     print("Please enter a valid integer.")
    print()

  elif num == 2:
    try:
     n = int(input("Enter the position of the Fibonacci number: "))
     if (n >= 0):
      print(f"The {n}th Fibonacci number is {fibonacci(n)}.")
     else:
      print("Please enter an integer greater than or equal to 0.")

    except:
     print("Please enter a valid integer.")
    print()

  # screen initializes the window for the drawing
  # pen is the variable used to move the turtle
  # Once the drawing is finished, user can click on the window and it will close
  elif num == 3:
    n = 100
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.setheading(90)
    spiral(pen, n)
    screen.exitonclick()
    print()

  elif num == 4:
    break
  
  else:
    print("Invalid option. Try again.")
    print()