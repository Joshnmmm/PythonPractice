import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Rock Paper Scissors")


bot = random.randint(0,2)

rps = [rock, paper, scissors]
choice = input("Choose between r, p, s: ")

if rps[bot] == rock: 
  print(rock)
  if choice == "r":
    print("TIE")
    print(rock)
  elif choice == "p":
    print("WIN")
    print(paper)
  elif choice == "s": 
    print("LOSE")
    print(scissors)

elif rps[bot] == paper: 
  print(paper)
  if choice == "r":
    print("LOSE")
    print(rock)
  elif choice == "p":
    print("TIE")
    print(paper)
  elif choice == "s": 
    print("WIN")
    print(scissors)

elif rps[bot] == scissors: 
  print(scissors)
  if choice == "r":
    print("WIN")
    print(rock)
  elif choice == "p":
    print("LOSE")
    print(paper)
  elif choice == "s": 
    print("TIE")
    print(scissors)