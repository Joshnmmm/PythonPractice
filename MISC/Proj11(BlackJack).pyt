import random 

print("Welcome to blackjack game\n")


J = 10 
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J"]

myCard = []
comCard = []

card1 = random.choice(cards)
card2 = random.choice(cards)
comCard1 = random.choice(cards)
comCard2 = random.choice(cards)

if card1 == "J": 
  card1int = 10
else: 
  card1int = card1
if card2 == "J": 
  card2int = 10
else: 
  card2int = card2


if comCard1 == "J": 
  comCard1int = 10
else: 
  comCard1int = comCard1
if comCard2 == "J": 
  comCard2int = 10
else: 
  comCard2int = comCard2 

comCard.append(comCard1int) 
comCard.append(comCard2int) 

myCard.append(card1int) 
myCard.append(card2int) 

myTotal = sum(myCard)
comTotal = sum(comCard)

print(f"Your cards: {myCard}")
print(f"The initial sum of your card is {myTotal}")
print(f"Computer cards: {comCard1int}")


def cardComparison(myTotal, comTotal): 
  if myTotal > 21: 
    print("You Lose nilapas ug 21")
  elif myTotal > comTotal:
    print("You win the bet :)")
  elif myTotal < comTotal: 
    print("You lose the bet :(")


user_input = input("type 'y' to get another card, 'n' to pass: ")
if user_input == "y": 
  myCard.append(random.choice(cards))
  print(myCard)
  myTotal = sum(myCard)
  print(f"The initial sum of your card is {myTotal}")
  print(f"Computer cards: {comCard1int}")
elif user_input == "n": 
  print(myCard)
  print(myTotal)
  print(comCard)
  print(comTotal)
  cardComparison(myTotal, comTotal)




