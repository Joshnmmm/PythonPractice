letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


eOrD = input("Encrypt or Decrypt: ")
numOfShift = int(input("Number of shift: "))
msg = input("Input your message: ")


def encrypt(msg, numOfShift):
  cipher_text = ""

  for letter in msg: 
    shifted_position = letters.index(letter) + numOfShift    #important
    shifted_position %= len(letters)
    cipher_text += letters[shifted_position]

  print(f"The encoded text is: {cipher_text}")

def decrypt(msg, numOfShift):
  cipher_text = ""

  for letter in msg: 
    shifted_position = letters.index(letter) - numOfShift    #important
    shifted_position %= len(letters)
    cipher_text += letters[shifted_position]

  print(f"The decoded text is: {cipher_text}")



if eOrD == "enc":
  encrypt(msg, numOfShift)
elif eOrD == "dec":
  decrypt(msg, numOfShift)
