def main():
    a = ["pizza", "tacos", "taquitos", "cheese", "pretzels"]
    for x in range(len(a)):
        print(a[x])
main()

first = input("What is your first name? ")
last = input("What is your last name? ")
print("Good day to you, " + first + " " + last + "!")

age = eval(input("How old are you? "))
print("Your age in days is about", (age * 365),".")
print("Your age in weeks is about",(age * 52.1429),".")
print("Your age in months is about", (age * 12),".")

noun = input("Enter a noun. ")
verb = input("Enter a verb. ")
adj = input("Enter an adjective. ")
loc = input("Enter a place. ")
print("The", adj, noun, verb + " at the " + loc)