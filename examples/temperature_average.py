
# Practice 01: Temperature Data Filtering

# Raw experimental measurements
temperatures = [0, None, 10, 20]

# Create an empty list for valid measurements
valid_temperatures = []

# Filter out missing measurements
for temperature in temperatures:
    if temperature is not None:
        valid_temperatures.append(temperature)

# Display the valid measurements
print("Valid temperatures:", valid_temperatures)

# Calculate average only when valid data exists
if len(valid_temperatures) > 0:
    average = sum(valid_temperatures) / len(valid_temperatures)
else:
    average = None

print("Average temperature:", average)