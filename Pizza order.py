#Code by Ekta Kapase

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

bill = 0;

#size

if size == "s":
  bill = 15
elif size== "m":
  bill = 20
elif size== "l":
  bill = 25
  
#pepperoni
  
if add_pepperoni == "y":
  if size=="s":
    bill +=2
  else:
    bill+= 3

#cheese
  
if extra_cheese == "y":
  bill +=1
  
#final_bill

print(f"Your final bill is {bill}.")
print("Thanks for ordering!")
