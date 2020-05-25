from machine_settings import *

"""
Method: machine_cycle()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST plugboard_config, STRING char, LIST rotors, INTEGER f_turn_amount, INTEGER m_turn_amount, INTEGER s_turn_amount
OUTPUT: string coded_char
FUNCTIONALITY:
- Controls the entire machine. It carries the character fed by the user through it.
"""


def machine_cycle(plugboard_config, char, rotors, offsets):
    # print("f_turn_amount", f_turn_amount, "m_turn_amount", m_turn_amount, "s_turn_amount", s_turn_amount)
    # print("char", char)
    char_plug_in = go_through_plugboard(plugboard_config, char)
    # print("char_plug_in:", char_plug_in)
    index_c_plug_in = ENGLISH_ALPHABET.index(char_plug_in)
    # print("index_c_plug_in:", index_c_plug_in)
    char_rotors_in = go_through_rotors_inwards(index_c_plug_in, rotors, offsets)
    # print("char_rotors_in:", char_rotors_in)
    char_reflector = reflector(char_rotors_in, offsets)
    # print("char_reflector:", char_reflector)
    index_c_reflector = ENGLISH_ALPHABET.index(char_reflector)
    # print("index_c_reflector:", index_c_reflector)
    char_rotors_out = go_through_rotors_outwards(index_c_reflector, rotors, offsets)
    # print("char_rotors_out:", char_rotors_out)
    index_char_rot_out = ENGLISH_ALPHABET.index(char_rotors_out)
    index_to_plug = (index_char_rot_out - offsets[0]) % ALPHABET_LENGTH
    char_rotors_out = ENGLISH_ALPHABET[index_to_plug]
    char_plug_out = go_through_plugboard(plugboard_config, char_rotors_out)
    # print("char_plug_out:", char_plug_out)
    coded_char = char_plug_out
    return coded_char


"""
Method: encrypt_char()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST list_text, LIST plugboard_config, LIST rotors, INTEGER f_turn_amount, INTEGER m_turn_amount, INTEGER s_turn_amount
OUTPUT: STRING coded_char
FUNCTIONALITY:
- Runs a single character through the entire system and returns the resulting coded version by calling machine_cycle()
"""


def encrypt_char(list_text, plugboard_config, rotors, offsets, i):
    char = list_text[i]
    coded_char = machine_cycle(plugboard_config, char, rotors, offsets)
    return coded_char


"""
Method: go_through_plugboard()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: LIST plugboard_config, STRING char
OUTPUT: STRING char_plug
FUNCTIONALITY:
- Establishes both the initial and the final phases of the encryption process.
- The plugboard connects two letters together so that if the user presses one of them,
it is converted into the other one and vice-versa.
"""


def go_through_plugboard(plugboard_config, char):
    list_conn_left = plugboard_config[0]
    list_conn_right = plugboard_config[1]
    char_plug = ""
    try:
        index = list_conn_left.index(char)
        char_plug = list_conn_right[index]
        return char_plug
    except ValueError:
        try:
            index = list_conn_right.index(char)
            char_plug = list_conn_left[index]
            return char_plug
        except ValueError:
            char_plug = char
            # print("")
            # print(char, "->", char_plug)
            # print("")
            return char_plug


"""
Method: go_through_rotors_in()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER index_c_plug_in, LIST rotors, INTEGER f_turn_amount, INTEGER m_turn_amount, INTEGER s_turn_amount
OUTPUT: STRING char_rotors_int
FUNCTIONALITY:
- Takes the index of the character that came from the plugboard and runs it through the rotors inwards up to the reflector piece.
- Returns the resulting character that will enter the reflector.
"""


def go_through_rotors_inwards(index_c_plug_in, rotors, offsets):
    char_plug = ENGLISH_ALPHABET[index_c_plug_in]
    index_c_plug_in = (index_c_plug_in + offsets[0]) % ALPHABET_LENGTH
    char_f_rot = go_fast_rotor_in(index_c_plug_in, rotors[0])
    index_c_f_rot = (ENGLISH_ALPHABET.index(char_f_rot) + offsets[1]) % ALPHABET_LENGTH
    char_m_rot = go_medium_rotor_in(index_c_f_rot, rotors[1])
    index_c_m_rot = (ENGLISH_ALPHABET.index(char_m_rot) + offsets[2]) % ALPHABET_LENGTH
    char_s_rot = go_slow_rotor_in(index_c_m_rot, rotors[2])
    index_c_s_rot = (ENGLISH_ALPHABET.index(char_s_rot) - offsets[3]) % ALPHABET_LENGTH
    char_s_rot = ENGLISH_ALPHABET[index_c_s_rot]
    # print((char_plug, "->", char_f_rot, "->", char_m_rot, "->", char_s_rot))
    char_rotors_in = char_s_rot
    return char_rotors_in




"""
Method: go_fast_rotor_in()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER index_c_plug_in, LIST list_f_rotor, INTEGER f_turn_amount
OUTPUT: STRING char_f_rotor
FUNCTIONALITY:
- Runs the character from the plugboard through the fast rotor.
- This method collects the position of the character in the alphabet,
adds the turn_amount from the rotation of the rotors and finds the character
that connects with the index in the fast rotor.
"""


def go_fast_rotor_in(index_c_plug_in, list_f_rotor):
    char = ENGLISH_ALPHABET[index_c_plug_in]
    # print(char)
    off_index = index_c_plug_in
    # print("off_index:", off_index)
    char_f_rotor = list_f_rotor[off_index]
    # print(ENGLISH_ALPHABET[off_index], "->", char_f_rotor)
    return char_f_rotor


"""
Method: go_medium_rotor_in()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER index_c_f_rot, LIST list_m_rotor, INTEGER m_turn_amount
OUTPUT: STRING char_m_rotor
FUNCTIONALITY:
- Runs the character from the fast rotor through the medium rotor.
- This method collects the position of the character in the alphabet,
adds the turn_amount from the rotation of the rotors and finds the character
that connects with the index in the medium rotor.
"""


def go_medium_rotor_in(index_c_f_rot, list_m_rotor):
    off_index = index_c_f_rot
    # print(char_index)
    char_m_rotor = list_m_rotor[off_index]
    # print(ENGLISH_ALPHABET[off_index], "->", char_m_rotor)
    return char_m_rotor


"""
Method: go_slow_rotor_in()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER index_c_m_rot, LIST list_s_rotor, INTEGER s_turn_amount
OUTPUT: STRING char_s_rotor
FUNCTIONALITY:
- Runs the character from the medium rotor through the slow rotor.
- This method collects the position of the character in the alphabet,
adds the turn_amount from the rotation of the rotors and finds the character
that connects with the index in the slow rotor.
"""


def go_slow_rotor_in(index_c_m_rot, list_s_rotor):
    off_index = index_c_m_rot
    # print(char_index)
    char_s_rotor = list_s_rotor[off_index]
    # print(ENGLISH_ALPHABET[off_index], "->", char_s_rotor)
    return char_s_rotor


"""
Method: reflector()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: STRING char_rotors_in
OUTPUT: STRING char_reflector
FUNCTIONALITY:
- Takes the character coming from the rotors to the reflector.
- Encodes the character with its corresponding connection.
- Sends the encoded character back to the slow rotor outwards.
"""


def reflector(char_rotors_in, offsets):
    char_index = ENGLISH_ALPHABET.index(char_rotors_in)
    char_reflector = REFLECTOR[char_index]
    # print("")
    # print(ENGLISH_ALPHABET[char_index], "->", char_reflector)
    # print("")
    return char_reflector


"""
Method: go_through_rotors_out()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER index_c_reflector, LIST rotors, INTEGER f_turn_amount, INTEGER m_turn_amount. INTEGER s_turn_amount
OUTPUT: STRING char_rou_out
FUNCTIONALITY:
- Runs the character from the reflector through the rotors again but in inverse order,
encoding it along the way up to the plugboard.
"""



def go_through_rotors_outwards(index_c_reflector, rotors, offsets):
    char_reflector = ENGLISH_ALPHABET[index_c_reflector]
    index_c_reflector = (index_c_reflector + offsets[3]) % ALPHABET_LENGTH
    char_s_rot = go_slow_rotor_out(index_c_reflector, rotors[2])
    index_c_s_rot = (ENGLISH_ALPHABET.index(char_s_rot) - offsets[2]) % ALPHABET_LENGTH
    char_m_rot = go_medium_rotor_out(index_c_s_rot, rotors[1])
    index_c_m_rot = (ENGLISH_ALPHABET.index(char_m_rot) - offsets[1]) % ALPHABET_LENGTH
    char_f_rot = go_fast_rotor_out(index_c_m_rot, rotors[0])
    char_rot_out = char_f_rot
    # print((char, "->", char_s_rot, "->", char_m_rot, "->", char_f_rot))
    return char_rot_out


"""
Method: go_slow_rotor_out()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER index_c_reflector, INTEGER s_turn_amount
OUTPUT: STRING char_s_rotor
FUNCTIONALITY:
- Runs the character from the reflector through the slow rotor.
- This method collects the position of the character in the slow rotor,
adds the turn_amount from the rotation of the rotors and finds the character
that connects with the index in the alphabet.
"""


def go_slow_rotor_out(index_c_reflector, list_s_rotor):
    # print(index_c_reflector)
    alpha_index = index_c_reflector
    char = ENGLISH_ALPHABET[alpha_index]
    index_in_rotor = list_s_rotor.index(char)
    # print(index_in_rotor)
    char_s_rotor = ENGLISH_ALPHABET[index_in_rotor]
    # print(char, "->", char_s_rotor)
    return char_s_rotor


"""
Method: go_medium_rotor_out()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER index_c_s_rot, INTEGER m_turn_amount
OUTPUT: STRING char_m_rotor
FUNCTIONALITY:
- Runs the character from the slow rotor through the medium rotor.
- This method collects the position of the character in the medium rotor,
adds the turn_amount from the rotation of the rotors and finds the character
that connects with the index in the alphabet.
"""


def go_medium_rotor_out(index_c_s_rot, list_m_rotor):
    # print(index_c_s_rot)
    alpha_index = index_c_s_rot
    char = ENGLISH_ALPHABET[alpha_index]
    index_in_rotor = list_m_rotor.index(char)
    char_m_rotor = ENGLISH_ALPHABET[index_in_rotor]
    # print(char, "->", char_m_rotor)
    return char_m_rotor


"""
Method: go_fast_rotor_out()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
INPUT: INTEGER index_c_m_rot, INTEGER f_turn_amount
OUTPUT: STRING char_f_rotor
FUNCTIONALITY:
- Runs the character from the medium rotor through the fast rotor.
- This method collects the position of the character in the fast rotor,
adds the turn_amount from the rotation of the rotors and finds the character
that connects with the index in the alphabet.
"""


def go_fast_rotor_out(index_c_m_rot, list_f_rotor):
    # print(index_c_m_rot)
    alpha_index = index_c_m_rot
    char = ENGLISH_ALPHABET[alpha_index]
    index_in_rotor = list_f_rotor.index(char)
    char_f_rotor = ENGLISH_ALPHABET[index_in_rotor]
    # print(char, "->", char_f_rotor)
    return char_f_rotor
