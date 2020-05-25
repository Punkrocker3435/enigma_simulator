from constants import *
import random


def random_key_generator():
    return [random_plugboard(), random_rotor_order(), random_rotor_position()]


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


def random_rotor_order():
    rotor_order = random.sample(range(1, 6), 3)
    return rotor_order


def random_rotor_position():
    random_positions = random.sample(range(UPPER_CASE_A_CODE, UPPER_CASE_Z_CODE + 1), 3)
    for i in range(len(random_positions)):
        random_positions[i] = chr(random_positions[i])
    return random_positions
