import logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(levelname)s - %(message)s')

def addition(a, b):
  print(f"\n{a} + {b} = {a + b}")

def subtraction(a, b):
  print(f"\n{a} - {b} = {a - b}")

def multiplication(a, b):
  print(f"\n{a} * {b} = {a * b}")

def division(a, b):
  print(f"\n{a} / {b} = {a / b}")

def firstNum():
  while True:
   try:
    a = int(input("Enter the first number: "))
    return a
   except ValueError as e:
    logging.error(f"ValueError in firstNum(): {e}")
    print("Invalid input! Please try a valid number.")

def secondNum():
  while True:
   try:
    b = int(input("Enter the second number: "))
    return b
   except ValueError as e:
    logging.error(f"ValueError in secondNum(): {e}")
    print("Invalid input! Please try a valid number.")

while True:
  try:
   num = int(input("\nMain menu:\n" \
   "1. Addition\n" \
   "2. Subtraction\n" \
   "3. Multiplication\n" \
   "4. Division\n" \
   "5. Exit\n"))

   if num == 1:
     addition(firstNum(), secondNum())

   elif num == 2:
     subtraction(firstNum(), secondNum())

   elif num == 3:
     multiplication(firstNum(), secondNum())

   elif num == 4:
     a = firstNum()
     while True:
       try:
         b = int(input("Enter the second number: "))
         if b == 0:
           raise ZeroDivisionError("Oops! Division by zero is not allowed.")
         
       except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError in division: {e}")
        print(e)

       except ValueError as e:
        logging.error(f"ValueError in division input: {e}")
        print("Invalid input! Please try a valid number.")

       else:
         division(a, b)
         break
       
   elif num == 5:
     print("Goodbye!")
     break
   
   else:
     print("Invalid input! Please try another number.")
     
  except ValueError as e:
     logging.error(f"ValueError in main menu: {e}")
     print("Invalid input! Please try a valid number.")
  