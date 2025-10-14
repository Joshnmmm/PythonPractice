print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice = input("left or right? ")
if choice == "left": 
  choice = input("swim or wait? ")
  if choice == "wait": 
    choice = input("Which door? ")
    if choice == "red":
      print("Fire game over")
    elif choice == "blue": 
      print("eat by beasts lol game over")
    elif choice == "yellow": 
      print("You win!")
  else: 
    print("shark eat game over")
else: 
  print("Fall into a hall. Game over.")