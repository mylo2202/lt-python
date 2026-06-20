"""
Exercise 5: Write a program which prompts the user for a Celsius tem
perature, convert the temperature to Fahrenheit, and print out the
converted temperature.
"""

celsius = input("Enter a temperature in Celsius: ")
fahrenheit = (float(celsius) * 1.8) + 32
print("Temperature in Fahrenheit: " + str(fahrenheit))
