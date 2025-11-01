import pandas 
temp_data = pandas.read_csv("temperature.csv")


temp_list = temp_data.temp.to_list()

sumOfTemperature = sum(temp_list)
averageOfTemperature = temp_data.temp.mean()
maxTemp = temp_data.temp.max()
minTemp = temp_data.temp.min()

print(sumOfTemperature)
print(averageOfTemperature)
print(maxTemp)
print(minTemp)

print(temp_data[temp_data.temp > 20])
print(temp_data[temp_data.temp == temp_data.temp.max()])
print(temp_data[temp_data.day == "Monday"])
