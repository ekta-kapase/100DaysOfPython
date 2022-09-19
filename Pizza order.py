#Code by Ekta Kapase
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1= name1.lower()
name2= name2.lower()
combined_name= name1 + name2

count_t = combined_name.count("t")
count_r = combined_name.count("r") 
count_u = combined_name.count("u") 
count_e = combined_name.count("e")

count_l = combined_name.count("l") 
count_o = combined_name.count("o")
count_v = combined_name.count("v")


tens_place = str(count_t + count_r + count_u + count_e)
ones_place = str(count_l + count_o + count_v + count_e)

score = (tens_place) +(ones_place)
score = int(score)

if 90<score<10:
  print(f"Your score is {score},you go together like coke and mentos.")
elif 40<score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
