# scraper.py
import requests
import pandas as pd
import os

# Define your API key and endpoint
API_KEY = '9451c4ce6fb1069fe1efbb2a58934436'
CITY = 'Berkeley'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information
        weather_data = {
            "date": [],
            "temperature": [],
            "humidity": [],
            "weather": []
        }
        for entry in data["list"]:
            weather_data["date"].append(entry["dt_txt"])
            weather_data["temperature"].append(entry["main"]["temp"])
            weather_data["humidity"].append(entry["main"]["humidity"])
            weather_data["weather"].append(entry["weather"][0]["description"])

        # Save data to a CSV file
        df = pd.DataFrame(weather_data)
        df.to_csv("weather_data.csv", index=False)
        print("Data saved to weather_data.csv")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_weather_data()
