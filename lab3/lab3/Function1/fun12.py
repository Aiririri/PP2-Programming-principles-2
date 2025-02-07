num = float(input("Enter the first number: "))
measure = (input("Enter 'C' for Celsius to Fahrenheit, 'F' for Fahrenheit toCelsius"))
if measure == "C":
    Fahrenheit = num * 9/5 + 32
    print(f" The value of {num} Celsius in Fahrenheit is: {Fahrenheit}")

elif measure == "F":
    Celsius = (num - 32) * 5/9
    print(f" The value of {num} Fahrenheit in Celsius is: {Celsius}")
else:
    print ("Error: Enter valid measuring system")

