print("welcome to BMI Calculator")

weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))

bmi = (weight / height ** 2) * 10000

bmi = round(bmi, 2)

print("Your BMI is " + str(bmi))


if bmi >= 25: 
  print("underweight")
elif bmi >= 18.5: 
  print("normal weight")
else:
  print("underweight")



