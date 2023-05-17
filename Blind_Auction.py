#Code by Ekta Kapase

from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Let's start bidding!!")

more_bidders = "yes"
bidding = {}
sold_bid = 0

while more_bidders != "no":
  name = input("\nWhat's your name? ")
  bid = int(input("What is your bid? Rs."))
  bidding[name] = bid
  more_bidders = input("\nAre there any more bidders? Yes or No : ").lower() 
  # -----Input done-----
  for bidder in bidding:
    price = bidding[bidder]
    if price > sold_bid:
      sold_bid = price
      winner = bidder
      
  clear()
  
# print(bidding)
print(f"\nThe winner is {winner} with the bid of Rs.{sold_bid} .🎉💐")
