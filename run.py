import random
import pyfiglet
import os

"""
    Cards for players
"""
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


"""
    Player and computer variables
"""
compHand = []
playerHand = []
playerIn = True
compIn = True


def welcome():
    """
    User welcome screen with menu
    """
    result = pyfiglet.figlet_format("Black Jack", "bubble")
    print(result)
    print("Welcome to Black Jack, a non-gambling game that utilizes the strategy elements of poker.\n") 
    print("Choose one of the options:")
    print("Press " + "1" + " to start game.")
    print("Press " + "2" + " Check the rules of the game.")
    print("Press" + " Q " + "to get out of the game.")
    option = False
    while not option:
        settings = input("\n")
        if settings == "1":
            option = True
            clear()
        elif settings == "2":
            option = True
            clear()
            rules()
        elif settings == "q": 
            print("Goodbye, see you soon ;)")
            exit()
        else:
            print("\n")
            print("Incorrect selected option")
            print("Please select one of the options provided\n")
            return welcome()


def rules():
    result = pyfiglet.figlet_format("R u l e s", "alligator")
    print(result)
    print(
        "The object of Black Jack is to get 21 points before your hand loses.",
        "\n The number of cards dealt to each player is chosen at random,",
        " and the player with the lowest hand is the dealer.\nIf you want ",
        "to learn more about Black Jack, there are many different advanced",
        " rules you can use on each game.\nThese rules include how many decks ",
        "need to be shuffled or lined up for a particular hand, what cards you",
        " hold or blackjack rules for double down after splitting aces.\n",
        "The rules of Black Jack are simple. ",
        "The dealer will deal two cards to each player,",
        " and then another card face up in the center of the table.",
        " Once all players have received their first two cards,",
        " they may choose to split or double down on those hands.\nAfter this",
        ", additional cards are dealt to players who have not yet received ",
        "their second card face up in front of them.The object in Black Jack",
        " is to get 21 points before your hand loses.\nThe number of cards",
        " dealt to each player is chosen at random and the player with the",
        " lowest hand is the dealer.\n")
    print("Press " + "E" + " to go back to the start menu")
    opt = False
    while not opt:
        settings = input("\n").lower().upper()
        if settings == "e":
            opt = True
            clear()
            return welcome()
        else:
            print("\n")
            print('If you want to leave the rules you have to press "E"')


def clear():
    os.system("clear")


def startGame(turn):
    """
    Random deal cards and remove cards from the deck
    """
    card = random.choice(cards)
    turn.append(card)
    cards.remove(card)


def scoring(turn):
    """
    Counting the score of the cards in the player's hand
    """
    score = 0
    faceCards = ["J", "Q", "K"]
    for card in turn:
        if card in range(1, 11):
            score += card
        elif card in faceCards:
            score += 1
        else:
            if score > 11:
                score += 1
            else:
                score += 11
    return score


def reportDelaerCards():
    """
    Reporting of drawn cards to the player and the computer
    """
    if len(compHand) == 2:
        return compHand[0]
    elif len(compHand) > 2:
        return compHand[0], compHand[1]


for _ in range(2):
    startGame(compHand)
    startGame(playerHand)

print(compHand)
print(playerHand)


while playerIn or compIn:
    """
    Display of cards and scores for player and computer with option to add card or stand
    """
    print(f"Delar had {compHand} for total of {scoring(compHand)} points.")
    print(f"User have {playerHand} for total of {scoring(playerHand)} points.")
    if playerIn:
        standOrHit = input("1: Stand\n2: Hit\n")
    if scoring(compHand) > 16:
        compIn = False
    else:
        startGame(compHand)
    if standOrHit == '1':
        playerIn = False
    else:
        startGame(playerHand)
    if scoring(playerHand) >= 21:
        break
    elif scoring(compHand) >= 21:
        break


"""
    Determination of win or loss for the players
"""
if scoring(playerHand) == 21:
    print("Black Jack !! You win :)")
    print(f"You win {playerHand} your opponent has {compHand}")
    print(f"You win, you had {scoring(playerHand)} points and your opponent only {scoring(compHand)} points")
elif scoring(compHand) == 21:
    print("Black Jack !! Dealer Wins :(")
    print(f"Unfortunately you lose your opponent has {compHand}  and you only {playerHand}")
elif scoring(playerHand) > 21:
    print("You give up ! Your opponent win :( ")
    print(f"Unfortunately you lose your opponent has {compHand}  and you only {playerHand}")
elif scoring(compHand) > 21:
    print(" You win !!! :)")
    print(f"You win {playerHand}  your opponent has {compHand}")
    print(f"You win, you had {scoring(playerHand)} points and your opponent only {scoring(compHand)}")
elif 21 - scoring(compHand) < 21 - scoring(playerHand):
    print("Dealer Wins!")
    print(f"Unfortunately you lose your opponent has {compHand} points and you only {playerHand}")
elif 21 - scoring(compHand) > 21 - scoring(playerHand):
    print("You win")
    print(f"You win, you had {playerHand}  and your opponent only {compHand}")
    print(f"You win, you had {scoring(playerHand)} points and your opponent only {scoring(compHand)}")