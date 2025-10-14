
def life_in_weeks(x):
  days = 90 - x
  weeks = days * 52
  print(f"You have {weeks} weeks remaining")



x = int(input("enter age: "))
life_in_weeks(x)
  