import random
num_to_guess = random.randint(1, 100)

counter = 0

# Since the bonus was to stop the game after 10 attempts, I used the counter as the looping condition
while counter < 10:
 num = int(input("Guess the number between 1 and 100: "))
 if num > num_to_guess:
  print("Too high! Try again.")
  counter += 1
 elif num < num_to_guess:
  print("Too low! Try again.")
  counter += 1
 else:
  print(f"Congratulations! You guessed it in {counter} attempts!")
  break     # ends the while loop once the number has been guessed

if counter == 10:
 print("Game over! Better luck next time!")
