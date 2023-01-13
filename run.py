import random

"""
    Cards for players
"""
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

"""
    Player and computer cards
"""
compHand = []
playerHand = []


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

