from constants import *
import re

"""
Method: prepare_text()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: STRING input_text
OUTPUT: STRING prepared_text
FUNCTIONALITY:
- Removes all special characters from the text before encoding can happen
"""


def prepare_text(input_text):
    replacements = [(r"Ä", "AE"), (r"Ö", "OE"), (r"Ü", "UE"), (r"Á", "A"), (r"É", "E"), (r"Í", "I"), (r"Ó", "O"), (r"Ú", "U"), (r"Ñ", "NI"), (r"_", ""),
                    (r"0", "ZERO"), (r"1", "ONE"), (r"2", "TWO"), (r"3", "THREE"), (r"4", "FOUR"), (r"5", "FIVE"), (r"6", "SIX"), (r"7", "SEVEN"),
                    (r"8", "EIGHT"), (r"9", "NINE"), (r'\+', '')]  # Regex and substitutions from list of tuples
    # Compile as regex objects, substitute regex as specified in the ordered dictionary
    prepared_text = input_text.upper()
    for rep_tuple in replacements:
        regex_pattern = re.compile(rep_tuple[0])
        rep = rep_tuple[1]
        prepared_text = regex_pattern.sub(rep, prepared_text)
    no_spaces = re.compile("[\s]+")
    no_special_chars = re.compile("[\W]+")
    prepared_text = re.sub(no_spaces, "", prepared_text)
    prepared_text = re.sub(no_special_chars, "", prepared_text)
    return prepared_text


"""
Method: place_rotors()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST_STRING rotor_order
OUTPUT: LIST_LIST rotors
FUNCTIONALITY:
- Places the rotors into the order specified by the user.
"""


def place_rotors(rotor_order):
    fast_rotor = list(NEW_ROTORS[int(rotor_order[0]) - 1][1])
    medium_rotor = list(NEW_ROTORS[int(rotor_order[1]) - 1][1])
    slow_rotor = list(NEW_ROTORS[int(rotor_order[2]) - 1][1])
    rotors = [fast_rotor, medium_rotor, slow_rotor]
    return rotors


"""
Method: set_rotors()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST initial_pos, LIST rotors
OUTPUT: LIST_INTEGER rotor_initial_position
FUNCTIONALITY:
- Turns the rotors into the desired initial positions.
"""


def set_rotors(initial_pos):
    f_rotor_setting = int(ENGLISH_ALPHABET.index(initial_pos[0]))
    m_rotor_setting = int(ENGLISH_ALPHABET.index(initial_pos[1]))
    s_rotor_setting = int(ENGLISH_ALPHABET.index(initial_pos[2]))
    rotor_initial_position = [f_rotor_setting, m_rotor_setting, s_rotor_setting]
    return rotor_initial_position


"""
Method: offset_calculator()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER f_pos_index, INTEGER m_pos_index, INTEGER s_pos_index
OUTPUT: LIST_4*INTEGER
FUNCTIONALITY:
- Calculates the difference between the rotor contacts. 
"""


def offset_calculator(f_pos_index, m_pos_index, s_pos_index):
    plug_f_offset = f_pos_index
    f_m_offset = (m_pos_index - f_pos_index) % ALPHABET_LENGTH
    m_s_offset = (s_pos_index - m_pos_index) % ALPHABET_LENGTH
    s_ref_offset = s_pos_index
    return [plug_f_offset, f_m_offset, m_s_offset, s_ref_offset]


"""
Method: get_double_step_position()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST key
OUTPUT: LIST_2*INTEGER
FUNCTIONALITY:
- Gets the position in which the medium and the slow rotor have to turn according to which rotor was selected to be placed into the machine.
"""


def get_double_step_position(key):
    # Take the index of the used rotors
    f_rotor = key[1][0] - 1
    m_rotor = key[1][1] - 1
    # print(f_rotor)
    # print(m_rotor)
    # Find the number in the DOUBLE STEP NOTCH table
    ds_setting = [DOUBLE_STEP_NOTCH[f_rotor][1] + 1, DOUBLE_STEP_NOTCH[m_rotor][1] + 1]
    return ds_setting


"""
Method: set_connections_amount()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: NONE
OUTPUT: INTEGER amount
FUNCTIONALITY:
- Prompts the user to enter the amount of connections they want to set on the plugboard.
"""


def set_connections_amount():
    while True:
        try:
            amount = int(input("Please, enter the amount of connections for the plugboard. MIN = 1, MAX = 13: "))
        except ValueError:
            print("Sorry, the input was invalid. Try again.")
            continue
        if amount < 1 or amount > 13:
            print("Sorry, the amount of connections must be between 1 and 13. Try again.")
            continue
        else:
            break
    return amount


"""
Method: set_plugboard()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: NONE
OUTPUT: LIST_2*LIST_STRING
FUNCTIONALITY:
- Calls set_conn_left() and set_conn_right().
- Checks for invalid inputs.
- Gathers results in a list.
"""


def set_plugboard():
    amount = set_connections_amount()
    list_conn_right = []
    list_conn_left = []
    while True:
        list_conn_left = set_conn_left(list_conn_left, amount)
        list_conn_right = set_conn_right(list_conn_right, amount)
        if is_overlapped(list_conn_left, amount) or is_overlapped(list_conn_right, amount):
            print(list_conn_left)
            print(list_conn_right)
            print("There is overlapping of connections. Try again.")
            list_conn_left = []
            list_conn_right = []
            continue
        elif invalid_amount_of_letters(list_conn_left) or invalid_amount_of_letters(list_conn_right):
            print(list_conn_left)
            print(list_conn_right)
            print("Only one letter can be on either side of the connection. Please, try again.")
            continue
        elif is_repeated(list_conn_left, list_conn_right):
            print(list_conn_left)
            print(list_conn_right)
            print("No letter can be connected to itself. Try again.")
            list_conn_left = []
            list_conn_right = []
            continue
        elif is_conn_invalid(list_conn_left, amount) or is_conn_invalid(list_conn_right, amount):
            print(list_conn_left)
            print(list_conn_right)
            print("There are invalid characters in the key. No numbers or special characters are admitted. Try again.")
            list_conn_left = []
            list_conn_right = []
            continue
        else:
            break
    is_repeated(list_conn_left, list_conn_right)
    return [list_conn_left, list_conn_right]


"""
Method: set_conn_left()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST list_conn_left, INTEGER amount 
OUTPUT: LIST list_conn_left
FUNCTIONALITY:
- Fills list_conn_left with user inputs.
"""


def set_conn_left(list_conn_left, amount):
    for i in range(amount):
        conn_left = input("Please, enter a letter on the left end of the connection: ")
        list_conn_left.append(conn_left.upper())
    return list_conn_left


"""
Method: set_conn_right()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST list_conn_right, INTEGER amount 
OUTPUT: LIST list_conn_right
FUNCTIONALITY:
- Fills list_conn_right with user inputs.
"""


def set_conn_right(list_conn_right, amount):
    for i in range(amount):
        conn_right = input("Please, enter a letter on the right end of the connection: ")
        list_conn_right.append(conn_right.upper())
    return list_conn_right


"""
Method: is_overlapped()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST connection, INTEGER amount 
OUTPUT: BOOLEAN
FUNCTIONALITY:
- Checks if a letter is connected to more than one other letter.
- It counts how many times each letter is present in one end of the connection and adds the total.
- If said total count exceeds the amount of set connections, it means there is overlapping.
"""


def is_overlapped(connection, amount):
    total_count = 0
    for letter in connection:
        total_count = total_count + connection.count(letter)
    return total_count > amount


"""
Method: is_repeated()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST connection_l, LIST connection_r
OUTPUT: BOOLEAN
FUNCTIONALITY:
- Looks for repetition in the connections, that is, if a letter is connected to itself.
- It forms a list that contains all the connections in form of a two-element list.
- Takes a connection and subtracts the ascii code of both elements, stores that result in INTEGER comparison
- Counts how many times INTEGER comparison equals 0.
- If the total count is not 0, it means that there is at least one letter connected to itself.
"""


def is_repeated(connection_l, connection_r):
    total = 0
    list_of_pairs = []
    for i in range(len(connection_l)):
        pair = [connection_l[i], connection_r[i]]
        list_of_pairs.append(pair)
    for letter_pair in list_of_pairs:
        comparison = ord(letter_pair[0]) - ord(letter_pair[1])
        if comparison == 0:
            total = total + 1
    return total != 0

"""
Method: is_conn_invalid()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST connection, INTEGER amount
OUTPUT: BOOLEAN
FUNCTIONALITY:
- Looks for special characters mistakenly entered when setting up connections by counting how many there are.
- Returns TRUE if a special char is found. Returns FALSE if no special chars are found.
"""

def is_conn_invalid(connection, amount):
    valid_count = 0
    for i in range(len(connection)):
        letter = connection[i]
        if (LOWER_CASE_A_CODE <= ord(letter) <= LOWER_CASE_Z_CODE) or (UPPER_CASE_A_CODE <= ord(letter) <= UPPER_CASE_Z_CODE):
            valid_count = valid_count + 1
    return valid_count != amount

"""
Method: invalid_amount_of_letters()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST list_connection
OUTPUT: BOOLEAN
FUNCTIONALITY:
- Counts how many entries are more than one char long.
- Returns TRUE if the count is not zero. Returns FALSE when all entries are exactly one char long.
"""
def invalid_amount_of_letters(list_connection):
    total_count = 0
    for i in range(len(list_connection)):
        if len(list_connection[i]) != 1:
            total_count = total_count + 1
    return total_count != 0

"""
Method: get_rotor_choice()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: NONE
OUTPUT: LIST_3*INTEGER rotor_order
FUNCTIONALITY:
- Prompts the user to choose which of the five rotors they want to use in the machine and in which order to place them.
"""

def get_rotor_choice():
    while True:
        try:
            fast_rotor = int(input("Please, input the number of the fast rotor (1-5): "))
            medium_rotor = int(input("Please, input the number of the medium rotor (1-5): "))
            slow_rotor = int(input("Please, input the number of the slow rotor (1-5): "))
        except ValueError:
            print("You should only enter numbers here. Try again, please")
            continue
        if rotor_doesnt_exist(fast_rotor, medium_rotor, slow_rotor):
            print("You have selected a rotor that doesn't exist. Please choose from rotors 1 to 5.")
            continue
        elif is_rotor_repeated(fast_rotor, medium_rotor, slow_rotor):
            print("You cannot use a rotor more than once. Please, try again.")
            continue
        else:
            break
    rotor_order = [fast_rotor, medium_rotor, slow_rotor]
    return rotor_order

"""
Method: rotor_doesnt_exist()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER fast_order, INTEGER medium_rotor, INTEGER slow_order
OUTPUT: BOOLEAN
FUNCTIONALITY:
- Counts how many times the user has entered a number less than 1 and greater than 5.
- Returns TRUE if there was a mistake. Returns FALSE if no errors were made.
"""

def rotor_doesnt_exist(fast_order, medium_rotor, slow_order):
    invalid_count = 0
    orders = [fast_order, medium_rotor, slow_order]
    for order in orders:
        if order < 1 or order > 5:
            invalid_count = invalid_count + 1
    return invalid_count != 0

"""
Method: is_rotor_repeated()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER fast_order, INTEGER medium_rotor, INTEGER slow_order
OUTPUT: BOOLEAN
FUNCTIONALITY:
- Returns TRUE if there is a repeated rotor. Returns FALSE if no repetition is found.
"""

def is_rotor_repeated(fast_rotor, medium_rotor, slow_rotor):
    return fast_rotor == medium_rotor or fast_rotor == slow_rotor or medium_rotor == slow_rotor

"""
Method: get_initial_rotor_position()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: NONE
OUTPUT: LIST_3*STRING
FUNCTIONALITY:
- Prompts the user to enter three letters symbolising the initial setting for all three rotors.
- Checks if user mistakenly entered a special character.
- Checks if user mistakenly entered more than three letters.
"""

def get_initial_rotor_position():
    invalid_data = 0
    while True:
        position = input("Please, enter the initial positions for the rotors ORDER = FAST MEDIUM SLOW. EXAMPLE = BUL: ")
        for char in position:
            if char.isdigit() or char.isspace() or char.isnumeric():
                invalid_data = invalid_data + 1
        if invalid_data != 0:
            print("You may only enter letters here. Try again.")
            continue
        elif len(position) != 3:
            print("This machine has 3 rotors, please enter their initial positions in order.")
            continue
        else:
            break
    return list(position.upper())


"""
Method: set_machine()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: STRING prepared_text, LIST_LIST key
OUTPUT: LIST settings
FUNCTIONALITY:
- Applies the configuration set by the user into the machine.
- Calls place_rotors() to order the rotors according to the user's command.
- Calls set_rotors() to set the initial positions of the three rotors.
"""


def set_machine(prepared_text, key):
    list_text = list(prepared_text)
    plugboard_config = key[0]
    rotor_order = key[1]
    rotors = place_rotors(rotor_order)
    rotor_initial_position = key[2]
    initial_turn_amount = set_rotors(rotor_initial_position)
    f_pos_index = initial_turn_amount[0]
    m_pos_index = initial_turn_amount[1]
    s_pos_index = initial_turn_amount[2]
    settings = [plugboard_config, rotors, f_pos_index, m_pos_index, s_pos_index]
    # print(settings)
    return settings
