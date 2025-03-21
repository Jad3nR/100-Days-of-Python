# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
more="yes"
bid_dictionary = {}
while more.lower()=="yes":
    name = input("What is your name?:  ")
    bid = int(input("What is your bid?:  "))
    bid_dictionary[name]=bid
    more=input("type yes for more bids, type no if no more bids ")
highest_bidder = max(bid_dictionary, key=bid_dictionary.get)
highest_bid = bid_dictionary[highest_bidder]

print(f"The highest bidder is {highest_bidder} with a bid of {highest_bid}.")