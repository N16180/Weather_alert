import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")
api_key = os.getenv("API_KEY")

url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 54.978252,
    "lon": -1.617780,
    "appid": api_key,
    "cnt" : 4
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for hour_data in data['list']:
    weather = hour_data['weather'][0]['id']
    if weather < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email, msg ="Subject: Its going to rain! \n\nBring an umbrella!")
