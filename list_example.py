country1 = "Australia"
country2 = "New Zealand"
country3 = "USA"
country4 = "England"

print(country1)
print(country2)
print(country3)
print(country4)

countries = ["Australia", "New Zealand", "USA", "England"]

print(countries)

# Prints Australia
print(countries[0])

# Replaces New Zealand with South Africa
countries[1] = "South Africa"

# Adds a new value to end of list
countries.append("New Zealand")

# Removes an item from the list
countries.remove("USA")

# Calculates the length of characters or the amount of items in a list
len(countries)

print("Total length of the list:", len(countries))