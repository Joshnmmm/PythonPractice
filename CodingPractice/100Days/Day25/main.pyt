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
print(data["day"])
print(data["temp"])

