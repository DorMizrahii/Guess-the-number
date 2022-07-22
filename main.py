#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).




import random
import art
from replit import clear

def guessing_game():
  print("Welcome to \"Guessing Game\" :)\n" + (art.logo))
  chosen_number = random.randint(1,100)
  level = input("What diffculty you want to play? 'easy' or 'hard'? ").lower()
  print("\n\n")
  if level == 'easy':
    life = 10
  elif level == 'hard':
    life = 5
  else:
    print("Please choose a correct level...(game exited)")
    return
    
  while life:
    print(f"You have {life} lifes!")
    guess = int(input("\n\nPlease guess a number between 1-100: "))
    if guess == chosen_number:
      print(f"\n\nGood job you win! the chosen number is: {chosen_number}.\n")
      break
    elif guess > chosen_number:
      print("Too High.\n")
      life -=1
    else:
      print("Too low.\n")
      life -=1
    print("\n\n")

    
  if not life:
    print(f"You lost :( the number was {chosen_number}\n\n")

    
  if input("Would like to start another game? type 'y' or 'n' ").lower() == 'y':
    clear()
    guessing_game()
    
    
guessing_game()
  
  