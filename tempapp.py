""" create a temperaure converter app that accepts a temperature in fahrenheit or celcius and returns the temperature in kelvin"""


def main():
    """ main function """
    print("Welcome to the temperature converter app")
    temp = float(input("Enter the temperature in Fahrenheit/Celcius: "))
    temp_type = input("Enter F for Fahrenheit or C for Celcius: ")
    temp_type = temp_type.upper()
    if temp_type == "F":
        kelvin = (temp + 459.67) * 5/9
        print(f"The temperature in Kelvin is {kelvin}Degrees Kelvin")
    elif temp_type == "C":
        kelvin = temp + 273.15
        print(f"The temperature in Kelvin is {kelvin} Degrees Celcius")
    else:
        print("You did not enter a valid temperature type")


if __name__ == "__main__":
    main()

