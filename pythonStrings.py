# Task 1
str = "Python is amazing!"
print(f"First word: {str[0:6]}")
print(f"Amazing part: {str[10:17]}")
print(f"Reversed string: {str[::-1]}")
print()

# Task 2
string = " hello, python world! "

# If this block is not not two separate lines, then the capitalize method
# does not work properly because the first character would be a space
string = string.strip()
print(f"Stripped string: {string}")

print(f"Capitalized string: {string.capitalize()}")
print(f"Replaced string: {string.replace("world", "universe")}")
print(f"Uppercase string: {string.upper()}")
print()

# Task 3
palindrome = input("Enter a string to check if it is a palindrome: ")

# palindrome[::-1] is the string but reversed
if palindrome == palindrome[::-1]:
 print(f"Yes, {palindrome} is a palindrome!")
else:
 print(f"No, {palindrome} is not a palindrome. Try another word!")