print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? Rs."))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

#Calculation

tip /= 100
bill_with_tip = (bill * (1 + tip))
bill_per_head = bill_with_tip / people
#contri_per_head = round(bill_per_head, 2)
contri_per_head = "{:.2f}".format(bill_per_head)
print(f"Each person shoud pay: Rs.{contri_per_head}")

print("Thank You!")
