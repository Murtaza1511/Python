from click import clear
from art import logo
print(logo)

def highest_bid_name(bidding_record):
    highest_bid = 0
    winner = None
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')


bids = {}
while True:
    name = input("What is your name?")
    bid_amount = int(input("What is your bid amount? $"))
    bids[name] = bid_amount
    isOtherBid = input("Are there any other bidder? Type 'yes' or 'no'. ")
    if isOtherBid == 'yes':
        clear()
        continue
    else:
        clear()
        break
highest_bid_name(bids)

# We can use pythontutor.com to visualise code and also help others with their bugs