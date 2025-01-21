print("Welcome to the tip calcalator!")
bill = float(input("What was the total bill? $"))
tip_in_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_peoples = int(input("How many people to split the bill? "))
tip = bill * (tip_in_percentage / 100)
total_bill = bill + tip
each_person_has_to_pay = round(total_bill / no_of_peoples, 2)
print(f"Each person should pay: ${each_person_has_to_pay}")
