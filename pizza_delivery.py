print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do  you want? S, M, L: ")
pepperoni  = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do  you want extra cheese on your pizza? Y or N: ").lower()

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif  size == "L":
    bill = 25
else:
    print("Invalid input")

if pepperoni == "y":
    if  size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your total bill is ${bill}.")
