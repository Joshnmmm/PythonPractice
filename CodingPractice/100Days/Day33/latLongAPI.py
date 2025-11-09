import requests
from datetime import datetime, timedelta


MY_LAT = 10.351932
MY_LONG = 123.913579

parameters = {
  "lat": MY_LAT,
  "lng": MY_LONG,
  "formatted": 0 
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters) # ---> Needed parameters via dictionary 

#print(response.status_code) error 400 for now cuz there are needed parameters to it (lat = data, long = data)
response.raise_for_status()

data = response.json()["results"]

# -------- Conversion of UTC to PH time ---------- #
utc_offset = timedelta(hours=8)
for key in ["sunrise", "sunset", "solar_noon"]:
    utc_time = datetime.fromisoformat(data[key])
    local_time = utc_time + utc_offset
    print(f"{key}: {local_time.strftime('%I:%M:%S %p')}")

