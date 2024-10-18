from db_operation import fetch_daily_summaries
import matplotlib.pyplot as plt

def display_visualizations():
    data = fetch_daily_summaries()
    
    # Example visualization of average temperatures
    cities = [row[0] for row in data]
    avg_temps = [row[2] for row in data]
    
    plt.bar(cities, avg_temps)
    plt.xlabel('City')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Daily Average Temperature by City')
    plt.show()
