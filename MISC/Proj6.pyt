import random

word_list = ["world", "bandage", "paper"]

random_word = random.choice(word_list)
print(random_word)

game_done = False
life = 0
correct_guess = False 

correct_letters = []

while not game_done:  
  guess = input("Input a letter: ").lower() 
  correct_guess = False 
  word_length = len(random_word)


  display = "" 

  for x in random_word: 
    if guess == x: 
      display += x 
      correct_letters.append(x)
      correct_guess = True
    elif x in correct_letters:
      display += x
    else:
      display += "_"

  if not correct_guess: 
    life += 1 
    print(f"Incorrect! You have {life} left")

  print(display)

  if "_" not in display:  #important 
    game_done = True 
    print("You win!")
  elif life == 3:  # Game over condition
      game_done = True  # Fix: Set game_done to True when losing
      print("You lose! The correct word was:", random_word)