import pytest
from pytest_bdd import scenario, given, when, then, parsers
from idioten_deck import create_deck


@pytest.fixture
def card_deck():
    deck = create_deck()
    assert len(deck) == 52
    return deck

@pytest.fixture
def previous_deck():
    previous_deck = create_deck()
    assert len(previous_deck) == 52
    return previous_deck


@scenario("idioten_deck.feature", "Deck is of the correct type")
def test_correct_type():
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", "Deck only contains allowed colours")
def test_allowed_colours():
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", "Deck only contains allowed ranks")
def test_allowed_ranks():
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", "Deck contains correct number of cards")
def test_correct_number_of_cards():
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", "Deck is different from previous deck")
def test_new_deck_different():
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", 'Deck contains no duplications')
def unique_card():
       Given no deck
       When deck shuffled
       Then deck contains no duplications


@given("existing deck")
def existing_deck(previous_deck):
    assert len(previous_deck) == 52
    assert type(previous_deck) == list


@when('deck shuffled')
def build_deck():
    card_deck = create_deck()
    assert type(card_deck) == list
    assert len(card_deck) == 52


@then('deck is of correct type')
def deck_type(card_deck):
    assert type(card_deck) == list


@then('deck contains only allowed colours')
def allowed_colour(card_deck):
    # Check that deck only contains allowed colours.
    allowed_colours = ["D", "S", "C", "H"]
    for i in range(len(card_deck)):
        assert card_deck[i][1] in allowed_colours


@then('deck contains only allowed ranks')
def allowed_rank(card_deck):
    allowed_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for i in range(len(card_deck)):
        assert card_deck[i][0] in allowed_ranks


@then('deck contains all cards')
def deck_length(card_deck):
    assert len(card_deck) == 52


@then('deck is different from previous deck')
def new_deck_previous_deck(card_deck, previous_deck):
    assert len(card_deck) == 52
    assert len(previous_deck) == 52
    assert card_deck != previous_deck


@then('deck contains no duplications')
def unique_card(card_deck):
    unique = []
    assert type(card_deck) == list
    assert len(card_deck) == 52
    for i in range(len(card_deck)):
        assert card_deck[i] not in unique
        unique.append(card_deck[i])



