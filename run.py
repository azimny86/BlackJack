import random
import pyfiglet
import os


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4

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
    print(
        "Welcome to Black Jack, a non-gambling game that utilizes the",
        " strategy elements of poker.\n")
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
        " rules you can use on each game.\nThese rules include how many decks",
        " need to be shuffled or lined up for a particular hand, what cards",
        " you hold or blackjack rules for double down after splitting aces.\n",
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
        settings = input("\n").lower()
        if settings == "e":
            opt = True
            clear()
            return welcome()
        else:
            print("\n")
            print('If you want to leave the rules you have to press "E"')


def clear():
    os.system("clear")


def deal(cards):
    """
    Random deal of cards
    """
    hand = []
    for _ in range(2):
        random.shuffle(cards)
        card = cards.pop()
        hand.append(card)
    return hand


def restart():
    """
    Restarting Game
    """
    info = input(
        "\nDo you want restart game ?\nY: Yes\nQ: Press any key\n").lower()
    if info == "y":
        clear()
    else:
        print("Goodbye, see you soon ;)")
        exit()


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


def hit(hand):
    """
    Handle hit option from the game
    """
    card = cards.pop()
    hand.append(card)
    return hand


def checkScore(compHand, playerHand):
    """
    Determination of win or loss for the players
    """
    if scoring(playerHand) == 21:
        print("Black Jack !! You win :)")
        print(f"You win {playerHand} your opponent has {str(compHand)}")
        print(
            f"You win, you had {scoring(playerHand)} points and"
            f" your opponent only {scoring(compHand)} points")
        restart()
    elif scoring(compHand) == 21:
        print("Black Jack !! Dealer Wins :(")
        print(
            f"Unfortunately you lose your opponent has {str(compHand)} "
            f"and you only {playerHand}")
        print(
            f"You lost, you had {scoring(playerHand)} points and your opponent"
            f" have {scoring(compHand)} points")
        restart()
    elif scoring(playerHand) > 21:
        print("You give up ! Your opponent win :( ")
        print(
            f"Unfortunately you lose your opponent has {str(compHand)}"
            f" and you only {playerHand}")
        print(
            f"You lost, you had {scoring(playerHand)} points and your"
            f" opponent have {scoring(compHand)} points")
        restart()
    elif scoring(compHand) > 21:
        print(" You win !!! :)")
        print(f"You win {playerHand}  your opponent has {str(compHand)}")
        print(
            f"You win, you had {scoring(playerHand)} points and your "
            f"opponent only {scoring(compHand)}")
        restart()
    elif 21 - scoring(compHand) < 21 - scoring(playerHand):
        print("Dealer Wins!")
        print(
            f"Unfortunately you lose your opponent has {str(compHand)} "
            f"points and you only {playerHand}")
        print(
            f"You lost, you had {scoring(playerHand)} points and your opponent"
            f" have {scoring(compHand)} points")
        restart()
    elif 21 - scoring(compHand) > 21 - scoring(playerHand):
        print("You win")
        print(
            f"You win, you had {playerHand}  and your "
            f"opponent only {str((compHand))}")
        print(
            f"You win, you had {scoring(playerHand)} points and your"
            f" opponent {scoring(compHand)}")
    elif scoring(playerHand) == scoring(compHand):
        print("Draw")
        restart()


def valdateInput(options):
    """
    Valideta input form game options
    """
    try:
        if options != "1" or "2" or "r" or "q":
            raise ValueError(
                "None of the options have been selected"
                )
    except ValueError as err:
        print(f"Invalid option use: {err}, please try again.\n")
        return False
    return True


def game(turn):
    """
    Running the game
    """
    options = 0
    compHand = deal(cards)
    playerHand = deal(cards)
    playerIn = True
    compIn = True
    print(f"Delar had {compHand} for total of {scoring(compHand)} points.")
    print(f"User have {playerHand} for total of {scoring(playerHand)} points.")
    scoring(compHand)
    scoring(playerHand)
    while playerIn or compIn:
        options = input("\n1: Stand\n2: Hit\nR: Restart\nQ: Quit\n").lower()
        if options == "1":
            playerIn = False
            hit(compHand)
            checkScore(compHand, playerHand)
            if scoring(compHand) > 16:
                compIn = False
            else:
                game(playerHand)
            if scoring(playerHand) >= 21:
                break
            if scoring(compHand) >= 21:
                break
        if options == "2":
            hit(playerHand)
            checkScore(compHand, playerHand)
            if scoring(compHand) > 16:
                compIn = False
            else: 
                game(playerHand)
            if scoring(playerHand) >= 21:
                break
            if scoring(compHand) >= 21:
                break
        elif options == 'r':
            restart()
        elif options == 'q':
            print("Goodbye, see you soon ;)")
            exit()
            break
        elif valdateInput(options):
            break


def main():
    welcome()


main()
