'''import csv

with open("weather_data.csv") as data_file:
  data = csv.reader(data_file)
  temperatures = [] 
  for i in data:
    if i[1] != 'temp':
      temperatures.append(i[1])
print(temperatures)'''

import pandas 
data = pandas.read_csv("weather_data.csv")


'''#print(data["day"])
#print(data["temp"])  or you can write data.temp // data.day



data_in_dict = data.to_dict() #converting datafile to dictionary 
#print(data_in_dict)
print(data["temp"].mean())
print(data["temp"].max())


#// operation on averaging it 
tempList = data["temp"].to_list()  #converting series it to list 
average = sum(tempList) / len(tempList)
print(average)'''


#print(data[data.temp == 14]) #printing a row with a data on that column 

print(data[data.temp == data.temp.max()])

monday_data = data[data.day == "Monday"] #assigning a variable to a specific row lang na data
temp = monday_data.temp  #printing the temperature only of the monday row nice


def celToFar(temp):
  return (temp* 9/5 ) + 32

print(celToFar(temp))


