import sqlite3
from datetime import datetime

DB_NAME = 'weather.db'

# Initialize database connection
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_summary (
                        city TEXT,
                        date TEXT,
                        avg_temp REAL,
                        max_temp REAL,
                        min_temp REAL,
                        dominant_weather TEXT)''')
    conn.commit()
    conn.close()

def store_daily_summary(weather_data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Aggregate daily weather data
    date = datetime.fromtimestamp(weather_data['timestamp']).strftime('%Y-%m-%d')
    
    cursor.execute('''INSERT INTO weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_weather)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (weather_data['city'], date, weather_data['temp'], weather_data['temp'],
                    weather_data['temp'], weather_data['main']))
    
    conn.commit()
    conn.close()

def fetch_daily_summaries():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM weather_summary")
    rows = cursor.fetchall()
    
    conn.close()
    return rows

def save_weather_data(city, weather_data):
    file_name = f"{city}_weather_data.txt"
    with open(file_name, 'a') as file:
        file.write(f"{weather_data}\n")
    print(f"Weather data for {city} saved to {file_name}")
