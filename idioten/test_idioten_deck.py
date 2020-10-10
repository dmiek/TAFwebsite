from pytest_bdd import scenario, given, when, then
from idioten_deck import create_deck

deck = []
previous_deck = []


@scenario("idioten_deck.feature", "Deck only contains allowed colours")
def test_create_deck():
    pass


@scenario("idioten_deck.feature", "Deck only contains allowed ranks")
def test_create_deck():
    pass


@scenario("idioten_deck.feature", "Deck is of the correct type")
def test_create_deck():
    pass


@scenario("idioten_deck.feature", "Deck contains correct number of cards")
def test_create_deck():
    pass


@scenario("idioten_deck.feature", "Deck is different from previous deck")
def test_create_deck():
    pass


@given("existing deck")
def test_existing_deck():
    previous_deck = create_deck()
    return previous_deck


@when('deck shuffled')
def new_deck_generated():
    deck = create_deck()
    assert type(deck) == list
    return deck


@then('deck contains only allowed colours')
def test_create_deck_allowed_colour():
    # Check that deck only contains allowed colours.
    allowed_colour = ["D", "S", "C", "H"]
    for i in deck:
        assert i[1] in allowed_colour


@then('deck contains only allowed ranks')
def test_create_deck_allowed_ranks():
    allowed_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for i in deck:
        assert i[0] in allowed_ranks


@then('deck is of correct type')
def test_deck_type():
    print(deck)
    assert type(deck) == list


@then('deck contains all cards')
def test_deck_length(deck):
    assert len(deck) == 52


@then('deck contains no duplications')
def test_unique_card():
    unique_card = []
    for i in range(len(deck)):
        assert deck[i] not in unique_card
        unique_card.append(deck[i])


@then('deck is different from previous deck')
def test_new_deck_previous_deck():
    assert deck != previous_deck





