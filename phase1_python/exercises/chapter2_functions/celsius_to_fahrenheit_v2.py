print("Celsius to fahrenheit converter")

def celsius_to_fahrenheit(celsuis): 
    return (celsuis  * (9 / 5)) + 32

celsuis = float(input("Enter celsius temp "))

print("Fahrenheit: ", celsius_to_fahrenheit(celsuis))