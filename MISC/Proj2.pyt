print("Welcome to the tip calculator")
total = input("What was the total bill? $")
tip = input("How much tip would you like to give?")
divide = input("How many people to split in the bill? ")
tip_value = float(total) * float(tip) * 0.01
tip_value += float(total)
final_amount = float(tip_value) / float(divide) 
final_amount = round(final_amount, 2)
print("Each person should pay: $" + str(final_amount))
