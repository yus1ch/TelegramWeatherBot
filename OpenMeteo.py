import requests

latitude = 44.5022 # широта
longitude = 34.1662 # долгота

link = "https://api.open-meteo.com/v1/forecast?latitude=44.5022&longitude=34.1662&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m&wind_speed_unit=ms"

r = requests.get(link).json()

print(r)