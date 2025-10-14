total_price = 0 


print("welcome to python pizza")
size = input("What pizza size do you want? S M L? ")
if size == "S":
  total_price += 15
elif size == "M":
  total_price += 20 
elif size == "L":
  total_price += 25 
else: 
  print("please input correct yes")

add_pep = input("Do you want pepperoni on you pizza? ")
if add_pep == "Y": 
  total_price += 2
else:
  total_price += 0 


print("Your total bill is: " + "$" + str(total_price))
