#Code by Ekta Kapase

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


print('''_____________________________________________
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|                         |.'.'.'.'.|
|.'.'.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'.'.'.|---|',             ,'|---|.'.'.'.'.|
|.'.'.'.'.|   |'.|___________|.'|   |.'.'.'.'.|
|.'.'.'.'.|   |'.|'.'.'.'.'.'|.'|   |.'.'.'.'.|
|,',',',',|   |',|.'.'.'.'.'.|,'|   |,',',',',|
|.'.'.'.'.|   |'.|'.'.'.'.'.'|.'|   |.'.'.'.'.|
|.'.'.'.'.|   |','   /%%%\   ','|   |.'.'.'.'.|
|.'.'.'.'.|   |'    /%%%%%\    '|   |.'.'.'.'.|
|.'.'.'.'.|Left%%%%%%%%%%%%%%%%Right|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;____________/%%%%%Start!%%%%%%\____________;|''')
choice1 = input("You are standing in a closed room with 2 exits, one to your left and other to your right. Which exit will you choose to start your treasure hunt? Left or Right -->\n ").lower()
if choice1 == "left":
  choice2 = input("You are out of room into mesmorizing nature facing a river across with a weak, frail bridge. Would you cross the river using by BRIDGE or WAIT for the boat ferry? Bridge or Ferry -->\n ").lower()
  if choice2 == "bridge":
    print('''                                                          
                                                          
                   ___###___________                      
            _,--"""_________________"""--._               
          /',--'\\"##           __  "//'--.'\   ,  /\    _
-._  /\  //'   ##\\       ,-_,-'  \_///\,-'`\\-' \/  \,-' 
   \/  \//    _  _\\ ,-._/         //'       \\           
       //'--._M_|H|\\___   ___   _//   ___   _\\   ___    
      | |    (|   | \\  | |   | |// | |   | | | | |   |   
   ___| |   /ooo=oo-o\\oo-oo=oo-//=oo-oo=oo-oo| |=oo=oo___
        \"'"'"'"'"'"'"'"'"'"'"'"'"'"'"'"'"'"'"|           
         |    \                           .   /           
   .      \   /\            .  -     '    .  /            
           `-.  '-..     ' '          ,  ,,-'     `       
              \     '- '            ,/,-'/                
    \          \_- ' '             --',-'                 
              -'                    \/            |       
     |  _  -                          - _        .       
                                                /       ''')
    
    choice3=input("You took the risk, but crossed the bridge safely. You continued the road for 1km nearing a cave. You entered the cave and saw 3 chests - Golden, Silver and Maroon. Which chest would you choose?\n ").lower()
    if choice3== "silver":
      print("Congratulations!!! You found the treasure!🪙")
    elif choice3== "golden":
      print("Bad luck! Your chosen chest is full of stones. Game over.")
    elif choice3 == "maroon":
      print("Bad luck! Your chosen chest is full of wood blocks. Game over.")
  
  elif choice2 == "ferry":
      print("Opps! Waiting for ferry caused you to be hungry lion pride's feast, you died and boom💥 you are out of your day dream😂")

elif choice1 =="right":
  print("Ohh! You entered a room full of poison, boom💥 you are out of your day dream😂.")
  
