# ltoc.py
# Aidan Perez 4/29/19
# Converts litres to cups, and vice versa.

def main():
    print("This program converts litres to cups, and cups to litres.")
    s = eval(input("Input 1 for litres to cups, 2 for the other way around. "))
    if s == 1:
        l = eval(input("What is the measurement in litres? "))
        c = l * 4.16
        print(c, "cups.")
        input("Hit enter to quit.")
    elif s == 2:
        c = eval(input("What is the measurement in cups? "))
        l = c / 4.16
        print(l, "litres.")
        input("Hit enter to quit.")
    else:
        input("you idiot. you fool. you absolute buffoon. that was not a 0 or a 1.")
main()