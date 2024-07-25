from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

bidders = {}
bid_is_over = False
name = ""
bid = 0
while not bid_is_over:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))

    bidders[name] = bid

    again = input("Are there any other bidders? yes or no: ")
    if again == "no":
        bid_is_over = True
    else:
        clear()

biggest_bidder = name
biggest_bid = bidders[biggest_bidder]
for bidder in bidders:
    if bidders[biggest_bidder] < bidders[bidder]:
        biggest_bidder = bidder
        biggest_bid = bidders[biggest_bidder]

print(f"The winner of the bid is {biggest_bidder} with ${biggest_bid}.")
        
    

    

