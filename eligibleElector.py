# Wrap the input in int() to conver input to a string
age = int(input("How old are you? "))

if age >= 18:
 print("Congratulations! You are eligible to vote. Go make a difference!")
else:
 # I used a printf() statement here for easy implementation of the age variable and calculation of how many years left go.
 print(f"Oops! You are not eligible yet. But hey, only {18-age} more year(s) to go!")