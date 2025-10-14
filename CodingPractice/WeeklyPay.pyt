#Create a program that asks for user's yearly pay and displays his weekly pay. 


totalNumber = int(input("Enter a number: "))
firstDigit = totalNumber%10
secondDigit = (totalNumber)//10 % 10 #integer division

sum = firstDigit + secondDigit

print(f"Your sum is: {sum}")
