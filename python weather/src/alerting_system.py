ALERT_THRESHOLD_TEMP = 35.0  # Example threshold for alerts

def check_alerts(weather_data):
    if weather_data['temp'] > ALERT_THRESHOLD_TEMP:
        trigger_alert(weather_data)

def trigger_alert(weather_data):
    print(f"Alert: {weather_data['city']} is experiencing high temperatures at {weather_data['temp']}°C.")
