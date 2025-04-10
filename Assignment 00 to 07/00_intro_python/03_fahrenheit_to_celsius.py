#Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
def temp_convertor():
    temp_in_fahrenheit = float(input("Enter temperature in Fahrenheit🌡: "))
    temp_in_celsius = (temp_in_fahrenheit - 32) * 5 / 9
    print(f"{temp_in_fahrenheit}°F is equal to {temp_in_celsius}°C.")

if __name__ == '__main__':
    temp_convertor()