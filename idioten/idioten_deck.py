import random


def createDeck():

    cardfaces = []
    suits = ["C", "D", "H", "S"]
    royals = ["A", "T", "J", "Q", "K"]
    deck = []

    for i in range(2,10):
        cardfaces.append(str(i))

    for j in range(len(royals)):
        cardfaces.append(royals[j])

    for k in range(len(suits)):
        for l in range(len(cardfaces)):
            card = (cardfaces[l] + suits[k])
            deck.append(card)
    random.shuffle(deck)
    return deck

deck = createDeck()
print(deck)




