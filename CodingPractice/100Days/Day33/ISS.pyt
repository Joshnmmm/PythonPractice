import requests 


'''
Status Code
1xx = Hold On 
2xx = Here you go 
3xx = Go Away
4xx = You screwed up (Like the error 404 smth)
5xx = I screwed up (the server)
'''

response = requests.get(url="http://api.open-notify.org/iss-now.json") # catching the API 
# print(response.status_code) # prints 200 so okay ra sha 

response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
timestamp = response.json()["timestamp"]

print(longitude)
print(latitude)
print(timestamp)






