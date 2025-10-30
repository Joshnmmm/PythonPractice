# Number game higher or lower guessing game 
# Function and scopes as well
import sys
import random

userAttempts = 0
randDigit = random.randrange(1,100)

difficulty = input("Enter wanted difficulty, 'easy' or 'hard':")
if difficulty == 'easy':
  userAttempts += 10
elif difficulty == 'hard': 
  userAttempts += 5 
else:
  print("Next time enter a valid choice srry :) ")

while userAttempts != 0: 
  guess = int(input("Guess a number from 1 - 100: "))
  if guess > randDigit: 
    print("Too high")
    userAttempts -= 1
  elif guess < randDigit: 
    print("Too low")
    userAttempts -= 1
  elif guess == randDigit: 
    print("Correct Nice")
    sys.exit(0)
  else:
    print("Enter a number lol XD")

print("You ran out of attempts sorry :( ")

