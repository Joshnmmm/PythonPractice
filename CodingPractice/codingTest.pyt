def mask_vowel_at_index (string, index):
  #if string[index] == "a" or string[index] == "e" or string[index] == "i" or string[index] == "u":
  if string[index] in "abeiou":
    newString = string[:index] + "*" + string[index+1:]
    print(newString)
  else:
    newString = string
    print(newString)

mask_vowel_at_index("abaca", 2)