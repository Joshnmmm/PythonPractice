#lesson 2 summary:
'''
def add(*args):  #this can accept any amount of arguments (this is not pointers)
  for n in args:
    print(n)           # looping all arguments

'''

# Write a code that adds all numbers as many passes as possible

def add(*args):
  sum = 0
  for n in args:
    sum +=n
  
  return sum

def maxSort(*args):
  large = args[0]
  for n in args:
    if n > large:
      large = n
  return large

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) #passed as many passes possible
print(maxSort(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) #passed as many passes possible

#can be good in sorting numbers 