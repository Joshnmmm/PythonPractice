import random
import sys

listofCards = [1,2,3,4,5,6,7,8,9,10,10,10]
yCard1 = random.choice(listofCards)
yCard2 = random.choice(listofCards)
cCard1 = random.choice(listofCards)
cCard2 = random.choice(listofCards)
youCards = [yCard1, yCard2]
comCards = [cCard1, cCard2]

print(f"Your cards: {youCards}")
print("Computer first card: ")


while (1):
  choice = input("Type 'y' to get another card, else 'n': ")
  if choice == 'y':
      youCards.append(random.choice(listofCards))
      youCardsTotal = sum(youCards)
      if youCardsTotal > 21: 
        print(youCards)
        print("You exceeded 21, lose auto :(")
        sys.exit(0)
      print(youCards)
  else:
    youCardsTotal = sum(youCards)
    break 
  
comCardsTotal = sum(comCards)
if comCardsTotal < youCardsTotal:
  print(f"Computer Cards:{comCards}")
  print("You win!")
elif comCardsTotal == youCardsTotal:
  print(f"Computer Cards:{comCards}")
  print("Tied!")
else:
  print(f"Computer Cards:{comCards}")
  print("You Lose")




