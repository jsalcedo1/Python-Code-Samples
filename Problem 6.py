# (Input) - Asks the user to enter temperature in Fahrenheit
temp = float(input("Enter temperature in Fahrenheit: "))
# (Process) - Calculates/determines Fahrenheit temperature in Celsius
celsius = (temp - 32) * 5/9
# (Output) -  Displays Fahrenheit temperature in Celsius
print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")
# (Notice) - Math formula - Celsius = (temperature - 32) x 5⁒9
