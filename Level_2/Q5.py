def analyze_temperatures(temperature_readings):
    """Analyzes temperature readings and returns the average, highest, and lowest temperatures."""
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    highest_temp = max(temperature_readings)
    lowest_temp = min(temperature_readings)
    return avg_temp, highest_temp, lowest_temp

if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter temperature readings, separated by spaces: ")

    temperature_readings = list(map(int, user_input.split()))

    average, highest, lowest = analyze_temperatures(temperature_readings)
    
    print(f"Average Temperature: {average}")
    print(f"Highest Temperature: {highest}")
    print(f"Lowest Temperature: {lowest}")