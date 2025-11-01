import pandas 
data = pandas.read_csv("states.csv")

states_list = data.state.to_list()



userPoints = 0
attempts = 10

while attempts != 0:
  userInput = input("Guess a State of thes America: ")
  if userInput in states_list:
    print("Correct")
    userPoints += 1
    print(f"Your points: {userPoints}")
    states_list.remove(userInput)
  else:
    attempts -= 1
    print("Wrong")

print("you lose")
