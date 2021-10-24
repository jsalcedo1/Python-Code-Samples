# 1.(Input)- Asks user to type the vehicle's miles driven
miles_driven = float(input('\nEnter number of miles driven: '))
gallons_of_gas_used = float(input('Enter gallons of gas used: '))

# 2. (Process) - Determines/calculates miles per galon
mpg = miles_driven / gallons_of_gas_used

# 3. (Output) - Displays the vehicle's miles per galon
print('In miles per gallon, your vehicle contains =', mpg, end='\n\n')
# (Notice) Math formula - mpg = miles driven ⁒ gallons used

