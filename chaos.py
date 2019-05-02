# File: chaos.py
# Created 4/29/19 by Aidan Perez
# Illustrates Chaotic Behavior.

def main(): # Function
    print("This program illustrates a chaotic function.") # Output
    x = float(input("Enter a number between 0 and 1. ")) # Input
    for i in range(10): # Loop
        x = 3.9 * x * (1 - x) # Assignment
        print(x) # Output
    
main()