def calculate_love_score(name1, name2):
  t = 0
  r = 0 
  u = 0 
  e = 0 
  l = 0 
  o = 0 
  v = 0 
  combined_name = name1 + name2 
  for char in combined_name: 
    if char == "t":
      t += 1
    elif char == "r": 
      r += 1 
    elif char == "u": 
      u += 1 
    elif char == "e": 
      e += 1 
    elif char == "l": 
      l += 1 
    elif char == "o": 
      o += 1 
    elif char == "v": 
      v += 1 
    elif char == "e": 
      e += 1 
  total1 = t + r + u + e 
  total2 = l + o + v + e 
  placeholder = "" 
  placeholder+=str(total1) 
  placeholder+=str(total2)
  print(placeholder)



name1 = input("Please input name1: ")
name2 = input("Please input name2: ")


calculate_love_score(name1, name2)


