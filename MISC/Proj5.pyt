import random 


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("welcome to password generator")

nu_letters = int(input(f"Please input number of letters: "))
nu_numbers = int(input(f"Please input number of numbers: "))
nu_symbols = int(input(f"Please input number of symbols: "))

password = []


for char in range(0, nu_letters):
  randomLet = random.choice(letters)
  password += randomLet

for char in range(0, nu_numbers):
  randomNum = random.choice(numbers)
  password += randomNum

for char in range(0, nu_symbols):
  randomSym = random.choice(symbols)
  password += randomSym


randomPass = password
random.shuffle(randomPass)

print(randomPass)

password_list= "" 
for char in password: 
  password_list += char

print(f"{password_list}")