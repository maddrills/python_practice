bides = [
    {
        "name" : "Mathew Francis",
        "bid" : 1500,
    },
    {
        "name": "Kamal Kahn",
        "bid": 100,
    },
    {
        "name": "George Francis",
        "bid": 1700,
    },
    {
        "name": "James Bons",
        "bid": 700,
    },
]

def highestBidCalculator(theBides):

    currentHighest = {
        "name" : "",
        "bid" : 0
    }

    # loop through the bids array
    for bidders in theBides:
        #then find the highest bidder
        if bidders["bid"] > currentHighest["bid"]:
            currentHighest = bidders

    print(currentHighest)

highestBidCalculator(bides)