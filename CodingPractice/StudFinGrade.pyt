#Determine a student's final grade and indicate whether it is passing or failing passing is 50
firstMark = int(input("Enter first mark: "))  
secMark = int(input("Enter second mark: "))  
thirMark = int(input("Enter third mark: "))  
fourMark = int(input("Enter fourth mark: "))

average = (firstMark + secMark + thirMark + fourMark)/4 


if average > 50 and average < 101: 
  print(f"Final Grade: {average}")
  print("Passed")
elif average < 50 and average > 0: 
  print(f"Final Grade: {average}")
  print("Failed")
else:
  print("Invalid Input")

