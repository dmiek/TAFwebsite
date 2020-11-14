Feature: Input
  The player input to the game. Module for testing Idioten input functionality.
  The input module takes input of length "1" only.


  Scenario Outline: Tests different input and asserts corresponding assessment returned
    Given input status is <startstate>
    When keyboard input of <inputvalue> is inserted
    Then input function should flag input as <endstate>

    Examples: Input values
    | startstate  | inputvalue  | endstate  |
    |   unknown   |     e       |   OK      |
    |   unknown   |     b       |   NOK     |
    |   unknown   |     .       |   NOK     |
    |   unknown   |     [       |   NOK     |
    |   unknown   |     d       |   OK      |
    |   unknown   |     dd      |   NOK     |
    |   unknown   |     5       |   NOK     |
    |   unknown   |     ee      |   NOK     |
    |   unknown   | dwdwadwadwa |   NOK     |
    |   unknown   | 43435435646 |   NOK     |
    |   unknown   |     1       |   OK      |
    |   unknown   |   hello     |   OK      |






