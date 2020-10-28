"""
Module for testing Idioten input functionality.
The input module takes input of length "1" only.
"""


from io import StringIO
from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_input import kb_input


@scenario(
    "features/idioten_input.feature",
    "Tests different input and asserts corresponding assessment returned",
    #example_converters=dict(start=str, eat=float, left=str)
)
def test_input_values():
    """
    Parsing table in feature in order to use as test input.
    Stating what type each component of the table is.
    """


@given("there are <startstate> cucumbers", target_fixture="start_input")
def start_input(startstate, input_fixture):
    """ Given game is waiting for input. """
    assert len(input_fixture) == 2
    assert len(input_fixture["keyboard"]) == 0
    assert input_fixture["status"] == 'unknown'
    assert input_fixture["keyboard"] == ''
    assert isinstance(startstate, str)
    return dict(start=startstate)


@when("I eat <inputvalue> cucumbers")
def eat_cucumbers(input_fixture, inputvalue, monkeypatch):
    """ When valid but too long input is given. """
    char_inputs = StringIO(inputvalue + '\n')
    monkeypatch.setattr('sys.stdin', char_inputs)
    temp_input = kb_input()
    input_fixture["keyboard"] = temp_input["keyboard"]
    input_fixture["status"] = temp_input["status"]
    assert isinstance(inputvalue, str)


@then("I should have <endstate> cucumbers")
def should_have_left_cucumbers(input_fixture, endstate):
    """ Verifying function returns correct values as stated in feature table. """
    assert isinstance(endstate, str)
    assert input_fixture["status"] == endstate
