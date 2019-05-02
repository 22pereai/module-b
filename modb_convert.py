# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan C.

def main():
    print("This program converts Celsius into Fahrenheit.")
    celsius = 0
    for i in range(11):
        fahrenheit = 9 / 5 * celsius + 32
        print(celsius, "degrees celsius is", fahrenheit, "degrees Fahrenheit.")
        celsius = celsius + 10
    s = eval(input("Input 1 to convert to fahrenheit, 2 to convert to celsius. "))
    if s == 1:
        for i in range(5):
            celsius = eval(input("What is the Celsius temperature? "))
            fahrenheit = 9 / 5 * celsius + 32
            print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        input("Hit enter to quit.")
    elif s == 2:
        for i in range(5):
            fahrenheit = eval(input("What is the Fahrenheit temperature? "))
            celsius = (fahrenheit - 32) * 5 / 9
            print("The temperature is", celsius, "degrees Celsius.")
        input("Hit enter to quit.")
    else:
        input("you idiot. you fool. you absolute buffoon. that was not a 0 or a 1.")
    

main ()
