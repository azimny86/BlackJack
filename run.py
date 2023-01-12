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