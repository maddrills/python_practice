############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#so the cards can be repeated
# if sum of cars is below 17 person must draw a card
# if it is over 21 person loses
# if person gets an ace he can regard the card to his favour as a 1 or an 11
# a random card is always delt to a person and dealer


# person object that holds the card info
persons = [];

# deal a random card
def deal():
    """Deals a random card when needed"""
    cardValue = int(random.random() * len(cards))
    # print("The Card "+theDeck[cardValue], cardValue)

    return cards[cardValue]

def game(name):
    """here is a dealer will draw a card one for himself and one for """
    persons.append({
        "name" : "Dealer",
        "cardValue" : 0,
    })

    persons.append({
        "name": name,
        "cardValue": 0,
    })


    val = input(f"Welcome {name} To Black Jack Press A to start")

    while val.lower() == "a":
        if(persons[0]["cardValue"] > 21):
            print("Player Wins")
            break
        if(persons[1]["cardValue"] > 21):
            print("Dealer Wins")
            break

        print(persons)
        drawCard = ""
        if persons[1]["cardValue"] == 0:
            drawCard = input("Press D to draw Or Press S to show")
        elif persons[1]["cardValue"] < 17:
            drawCard = input("Draw another Card with D")
        else:
            drawCard = input("Press D to draw Or Press S to show")

        if drawCard.lower() == "d":
            # if the dealer is below 17
            if persons[0]["cardValue"] < 17:
                ace = deal()
                if ace == 11 and persons[1]["cardValue"] + ace > 21:
                    persons[0]["cardValue"] += 1
                elif ace == 11:
                    persons[0]["cardValue"] += 11
                else :
                    persons[0]["cardValue"] += ace

            elif persons[0]["cardValue"] < 21:
                persons[0]["cardValue"] += deal()
            else:
                "You Win"
                break

            #if person falses short
            if persons[1]["cardValue"] < 17:
                ace = deal()
                print(ace)
                if ace == 11 and persons[1]["cardValue"] + ace > 21:
                    persons[1]["cardValue"] += 1
                elif ace == 11:
                    persons[1]["cardValue"] += 11
                else :
                    persons[1]["cardValue"] += ace

            elif persons[1]["cardValue"] < 21:
                persons[1]["cardValue"] += deal()
            else:
                "Dealer Wins"
                break


            continue
        elif drawCard.lower() == "s":
            if persons[0]["cardValue"] > 17 and persons[0]["cardValue"] > 17:
                if persons[0]["cardValue"] < persons[1]["cardValue"]:
                    print(f"{persons[1]} Wins")
                elif persons[0]["cardValue"] > persons[1]["cardValue"]:
                    print(f"{persons[0]} Wins")
                else:
                    print(f"{persons[0]} and {persons[1]} have the same Value its a Draw")
                break
            else:
                continue

        else:
            print("Invalid Input")
            continue



if __name__ == "__main__":
    print("Main Call")

    name = input("Enter You Name")
    game(name)
