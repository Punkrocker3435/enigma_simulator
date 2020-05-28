from constants import *
import random

"""
Method: random_key_generator()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: NONE
OUTPUT: LIST_3*LIST
FUNCTIONALITY:
- Returns a list of three elements.
- 1st, plugboard connections.
- 2nd, rotor order.
- 3rd, rotor initial positions.
"""
def random_key_generator():
    return [random_plugboard(), random_rotor_order(), random_rotor_position()]

"""
Method: random_plugboard()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: NONE
OUTPUT: LIST_2*LIST_amount*STRING
FUNCTIONALITY:
- Generates a random number between 1 and 13 called "amount"
- Generates a list, "random letters", of random non-repeating numbers between the codes for the uppercase alphabet letters with 2*amount elements.
- Splits that list into two lists of equal size.
- Puts those lists into another list and returns it.
"""
def random_plugboard():
    amount = random.randint(1, 13)
    random_letters = random.sample(range(UPPER_CASE_A_CODE, UPPER_CASE_Z_CODE + 1), 2 * amount)
    for i in range(len(random_letters)):
        random_letters[i] = chr(random_letters[i])
    list_conn_left = random.sample(random_letters, amount)
    for i in range(amount):
        random_letters.remove(list_conn_left[i])
    list_conn_right = random_letters
    return [list_conn_left, list_conn_right]

"""
Method: random_rotor_order()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: NONE
OUTPUT: LIST_3*INTEGER rotor_order
FUNCTIONALITY:
- Uses random module to generate a list of three random non-repeating numbers from 1 to 5 and returns it.
"""
def random_rotor_order():
    rotor_order = random.sample(range(1, 6), 3)
    return rotor_order

"""
Method: random_rotor_position()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: NONE
OUTPUT: LIST_3*STRING random_positions
FUNCTIONALITY:
- Uses random module to generate a list of three letters from the uppercase alphabet and returns it.
"""
def random_rotor_position():
    random_positions = random.sample(range(UPPER_CASE_A_CODE, UPPER_CASE_Z_CODE + 1), 3)
    for i in range(len(random_positions)):
        random_positions[i] = chr(random_positions[i])
    return random_positions
