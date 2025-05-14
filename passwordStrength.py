password = input("Enter a password to have its strength checked: ")
counter = 0

if len(password) < 8:
 print("Your password must be at least 8 characters.")
 counter += 1

if not any (ch.isupper() for ch in password):
 print("Your password needs at least one uppercase letter.")
 counter += 1

if not any (ch.islower() for ch in password):
 print("Your password needs at least one lowercase letter.")
 counter += 1

if not any (ch.isdigit() for ch in password):
 print("Your password needs at least one digit.")
 counter += 1

# .isalnum() returns false if a character is not alphanumeric
# .isspace() returns false if a character is not a space
# I want to allow spaces in my passwords, which is why I put in the .isspace() part
if all (ch.isalnum() or ch.isspace() for ch in password):
 print("Your password needs at least one special character.")
 counter += 1

# Strength meter
if counter == 5:
 print("Your password scores 0/5, very weak and not allowed.")
if counter == 4:
 print("Your password scores 1/5, weak and not allowed.")
if counter == 3:
 print("Your password scores 2/5, okay and not allowed.")
if counter == 2:
 print("Your password scores 3/5, decent and now allowed.")
if counter == 1:
 print("Your password scores 4/5, strong and not allowed.")
if counter == 0:
 print("Your password scores 5/5, very strong and allowed.")


