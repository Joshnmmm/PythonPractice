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




#lesson 3: kwargs 
print("")
def calculate(n, **kwargs): #unli keyword arguments 
  #basically it returns a dictionary 
  print(kwargs)
  '''
  for key, value in kwargs.items():
  
    print(key)
    print(value)
    '''
  n+= kwargs["add"]
  n*= kwargs["multiply"]
  print(n) 
  


calculate(2, add = 3, multiply=5)
#passed 2, added 3, multiplied it by 5
# 2 + 3 = 5, 5*5 = 25

# the purpose of kwargs is like in our JAVA oop, pwede ta ka create ug object with multiple, one, or none (this thing)
# mura shag kanang naa sa REACT programing language: 
# <input type=form style=bold > etc etc