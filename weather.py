print("=== Temperature Checker ===")
temperature = float(input("Enter the temperature in Celsius: "))

# IF temperature is less than 0, THEN it is freezing
if temperature < 0:
    print(f"Then {temperature}°C is FREEZING! ❄️")

# IF temperature is between 0 and 10, THEN it is very cold
if temperature >= 0 and temperature < 10:
    print(f"Then {temperature}°C is VERY COLD ❄️")

# IF temperature is between 10 and 20, THEN it is cold
if temperature >= 10 and temperature < 20:
    print(f"Then {temperature}°C is COLD 🧊")

# IF temperature is between 20 and 25, THEN it is cool
if temperature >= 20 and temperature < 25:
    print(f"Then {temperature}°C is COOL 😌")

# IF temperature is between 25 and 30, THEN it is warm
if temperature >= 25 and temperature < 30:
    print(f"Then {temperature}°C is WARM ☀️")

# IF temperature is between 30 and 35, THEN it is hot
if temperature >= 30 and temperature < 35:
    print(f"Then {temperature}°C is HOT 🔥")

# IF temperature is 35 or above, THEN it is very hot
if temperature >= 35:
    print(f"Then {temperature}°C is VERY HOT 🌡️")

# Show recommendations
print("\n--- Recommendations ---")

if temperature < 0:
    print("Then wear heavy winter clothes!")

if temperature >= 0 and temperature < 10:
    print("Then wear a warm coat and gloves!")

if temperature >= 10 and temperature < 20:
    print("Then wear a jacket or sweater!")

if temperature >= 20 and temperature < 25:
    print("Then a light jacket might be nice!")

if temperature >= 25 and temperature < 30:
    print("Then wear a t-shirt - perfect weather!")

if temperature >= 30 and temperature < 35:
    print("Then wear light, breathable clothes!")

if temperature >= 35:
    print("Then stay hydrated and seek shade!")

# Convert to Fahrenheit
fahrenheit = (temperature * 9/5) + 32
print(f"\nThen in Fahrenheit, that's {fahrenheit:.1f}°F")