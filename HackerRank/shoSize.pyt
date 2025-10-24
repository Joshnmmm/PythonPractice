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




