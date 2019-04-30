# ktom.py
# Aidan Perez 4/29/19
# Converts kilometers to miles, and vice versa.

def main():
    print("This program converts kilometers to miles, and miles to kilometers.")
    s = eval(input("Input 1 for kilometers to miles, 2 for the other way around. "))
    if s == 1:
        kilo = eval(input("What is the measurement in kilometers? "))
        mile = kilo * 0.62
        print(mile, "miles.")
        input("Hit enter to quit.")
    elif s == 2:
        mile = eval(input("What is the measurement in miles? "))
        kilo = mile * 1.6
        print(kilo, "kilometers.")
        input("Hit enter to quit.")
    else:
        input("you idiot. you fool. you absolute buffoon. that was not a 0 or a 1.")
main()