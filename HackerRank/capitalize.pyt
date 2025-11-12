
def solve(user_input):
  final_word = ""
  words =user_input.split(" ")
  for word in words:
      if word:
          final_word += word[0].upper() + word[1:] + " "
      else:
          final_word += " "
  
  return(final_word)



user_input = input("Please input word: ")

solve(user_input)
print(user_input)

#print(final_word.rstrip())
