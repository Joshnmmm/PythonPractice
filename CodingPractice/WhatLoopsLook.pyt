#Average of even numbers and product of odd number, 10 integers


sum = 0 
for i in range(100): #for(int i=0; i<5; i++)
  sum += i+1
'''
for f in range(1, 6):  #for (i = 1; i >= 5; i++)
    print(f)'''

# (0, 0, 0) ==== start, stop, step

'''
for i in range(2, 11, 2): #printing even from 2 - 10 
   print(i)'''

n = 5  # number of rows

for row in range(1, n + 1):
    # print spaces
    for space in range(n - row):
        print(" ", end="")

    # print stars
    for star in range((2 * row) - 1):
        print("8", end="")

    # move to next line
    print()