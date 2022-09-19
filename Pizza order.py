#Code by Ekta Kapase
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0;

#size

if size == "S":
  bill = 15
elif size== "M":
  bill = 20
elif size== "L":
  bill = 25
  
#pepperoni
  
if add_pepperoni == "Y":
  if size=="S":
    bill +=2
  else:
    bill+= 3

#cheese
  
if extra_cheese == "Y":
  bill +=1
  
#final_bill

print(f"Your final bill is {bill}.")
print("Thanks for ordering!")



