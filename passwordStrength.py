password = input("Enter a password to have its strength checked: ")

if not any (ch.isupper() for ch in password):
 print("Your password needs at least one uppercase letter.")

if not any (ch.islower() for ch in password):
 print("Your password needs at least one lowercase letter.")

if not any (ch.isdigit() for ch in password):
 print("Your password needs at least one digit.")

# .isalnum() returns false if a character is not alphanumeric
# .isspace() returns false if a character is not a space
# I want to allow spaces in my passwords, which is why I put in the .isspace() part
if all (ch.isalnum() or ch.isspace() for ch in password):
 print("Your password needs at least one special character.")


