#Code by Ekta Kapase
year = int(input("Which year do you want to check? "))

if year % 4 ==0:
    if year % 100 != 0:
        print("Leap year.")
        
#Opt1 This -->  
#1<--------------------------------------------------------->
    else:
        print("Leap year.")

elif year % 400 == 0: # divisible by both 100 and 400  
    print("Leap year.")
#1<--------------------------------------------------------->


#2 or this ---> (easy explanation)
#2<--------------------------------------------------------->
    # elif year % 100 ==0:
    #     if year % 400 == 0:
    #         print("Leap year.")
    #     else:
    #         print("Not leap year")

    # else:
         # print("Leap year.")
#2<--------------------------------------------------------->
        
else:
    print("Not leap year.")
