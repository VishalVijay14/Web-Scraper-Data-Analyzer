# data_analyzer.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("weather_data.csv")

# Data Analysis: Basic statistics
def analyze_data():
    print("Summary Statistics:")
    print(df.describe())

    # Average temperature and humidity
    avg_temp = df["temperature"].mean()
    avg_humidity = df["humidity"].mean()
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Average Humidity: {avg_humidity:.2f}%")

# Data Visualization: Temperature and Humidity Trends
def visualize_data():
    plt.figure(figsize=(12, 6))
    
    # Plot temperature over time
    sns.lineplot(data=df, x="date", y="temperature", marker="o", label="Temperature (°C)")
    plt.xticks(rotation=45)
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Plot humidity over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="date", y="humidity", marker="o", color="orange", label="Humidity (%)")
    plt.xticks(rotation=45)
    plt.title("Humidity Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analyze_data()
    visualize_data()
