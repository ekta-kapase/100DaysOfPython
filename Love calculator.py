print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1= name1.lower()
name2= name2.lower()
count_t = name1.count("t") + name2.count("t")
count_r = name1.count("r") + name2.count("r")
count_u = name1.count("u") + name2.count("u")
count_e = name1.count("e") + name2.count("e")

count_l = name1.count("l") + name2.count("l")
count_o = name1.count("o") + name2.count("o")
count_v = name1.count("v") + name2.count("v")


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
