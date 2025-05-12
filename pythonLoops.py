# Task 1
age = int(input("Enter a number: "))
while age > 0:
 print(age, end = " ")
 age -= 1     # this subtracts 1 from age and sets age equal to the result
print("Blast off!")

# Task 2
num = int(input("Enter a number: "))
for i in range(1, 11):
 print(f"{num} x {i} = {num * i}", end = " ")
print()

# Task 3
factorial = int(input("Enter a number: "))
sum = 1
for i in range(1, factorial + 1):
 sum *= i     # this multiplies sum by i and sets sum equal to the result
print(f"The factorial of {factorial} is {sum}")