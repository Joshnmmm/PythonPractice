# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

total = 0
X = int(input()) 
my_list_int = list(map(int, input().split())) 
N = int(input())

for i in range(N):
  EnEx = list(map(int, input().split())) 
  if EnEx[0] in my_list_int:
    my_list_int.remove(EnEx[0])
    total += EnEx[1]
  else:
    print("no hello world")


print(total)



'''my_fruit = ['apple', 'banana', 'mango', 'banana', 'apple', 'banana']
counting = Counter(my_fruit)

print(counting.most_common(1))
print(counting)


for fruit in counting:
  if counting[fruit] > 1:
    print("Greater than 1")
  else:
    print("Not Greated than 1")
'''

'''
letter = input()
counted = Counter(list(letter))


for letters in counted:
  if counted[letters] > 1:
    print(f"{letters}: {counted[letters]}")

print(counted.most_common(1))'''