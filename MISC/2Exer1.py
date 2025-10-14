#Bmi Calculator
weight = input("Please enter your weight: ")
height = input("Please enter your height: ")

bmi = float(weight) / (float(height) ** 2)

print("Your BMI is " + str(bmi))


