import time
from encryption_decryption import *
from machine_settings import *
from random_key_generator import *
from file_handling import *


def main():
    print(PROGRAM_NAME)
    print("-" * 140)
    print("Welcome to the Enigma Machine Simulator v1")
    print("")
    print("This is a cmd version of the Enigma Machine used by the Germans during World War II to communicate secretly.")
    print("This particular program simulates the Enigma used by the Wehrmacht, first introduced in 1930 and used before and during the entire war.")
    print("Other versions of the Enigma were available for both commercial and military use.")
    print("-" * 140)
    print("")
    while True:
        print_basic_menu()
        try:
            user_choice = int(input("Choose an option: "))
        except ValueError:
            print("Sorry, your input was invalid. Try again.")
            continue
        if user_choice == 1:
            put_machine_to_work()
            continue
        else:
            clear_used_key()
            clear_used_text()
            break


def put_machine_to_work():
    # Machine is being set
    coded_text = ""
    key = get_key()
    input_text = get_input_text()
    prepared_text = prepare_text(input_text)
    settings = set_machine(prepared_text, key)
    list_text = list(prepared_text)
    plugboard_config = settings[0]
    rotors = settings[1]
    f_pos_index = settings[2]
    m_pos_index = settings[3]
    s_pos_index = settings[4]
    rot_pos_indexes_list = [f_pos_index, m_pos_index, s_pos_index]
    double_step_notch = get_double_step_position(key)
    # Machine setting is completed.

    # Animation showing machine setting
    animation_plugboard(key)
    print("")
    animation_rotors_choosing(key)
    print("")
    animation_rotors_turning(rot_pos_indexes_list)
    print("")
    # End of animation

    # Encryption process begins.
    for i in range(len(prepared_text)):
        rot_pos_indexes_list = turn_rotor(rot_pos_indexes_list, double_step_notch)
        f_pos_index = rot_pos_indexes_list[0]
        m_pos_index = rot_pos_indexes_list[1]
        s_pos_index = rot_pos_indexes_list[2]
        offsets = offset_calculator(f_pos_index, m_pos_index, s_pos_index)
        coded_char = encrypt_char(list_text, plugboard_config, rotors, offsets, i)
        coded_text = coded_text + coded_char
    # Encryption process completed. Both the plaintext and the encoded text are going to be displayed on screen.

    print_key(key)
    print("Plaintext:", input_text)
    print("")

    # Adding spaces every 4 characters to resemble an actual message from the times of WWII.
    print("Encrypted text:", add_spaces(coded_text, 4))
    print("")

    # Favourites time!
    add_favourite_key(key)
    add_favourite_text(input_text)
    print("")


def get_input_text():
    while True:
        print("1 - Type text to encrypt.")
        print("2 - Use favourites list.")
        try:
            user_choice = int(input("Choose an option: "))
        except ValueError:
            print("Sorry, your choice was invalid. Please enter only numbers.")
            continue
        if user_choice == 1:
            text = input("Please, enter the text you want to encrypt: ")
            add_used_text(text)
            break
        elif user_choice < 1 or user_choice > 2:
            print("Sorry, there is no {}th option. Try again".format(user_choice))
            continue
        elif user_choice == 2:
            print("-" * 50)
            list_fav_texts = print_fav_text()
            for i in range(len(list_fav_texts)):
                print("{} - {}".format(i + 1, list_fav_texts[i]))
            print("-" * 50)
            text = get_favourite_text(list_fav_texts)
            break
        else:
            break
    input_text = text.upper()
    return input_text


def get_key():
    print("You are now configuring the key to encrypt the message.")
    key = []
    while True:
        try:
            user_choice = int(input(
                "Do you want to set your own key? (press 1)\n... or do you want a randomly generated one? (press 2)\n... or maybe use the default key (press "
                "3)\n...OK, maybe check the favourite keys list? (press 4): "))
        except ValueError:
            print("Sorry, your input was invalid. You need to enter a valid option.")
            continue
        if user_choice < 1 or user_choice > 4:
            print("Sorry, there is no option", user_choice, ". Please choose between 1, 2 or 3.")
            continue
        if user_choice == 1:
            plugboard_config = set_plugboard()
            rotor_order = get_rotor_choice()
            rotor_initial_position = get_initial_rotor_position()
            key.append(plugboard_config)
            key.append(rotor_order)
            key.append(rotor_initial_position)
            break
        elif user_choice == 2:
            key = random_key_generator()
            break
        elif user_choice == 3:
            key = [[["Y"], ["Z"]], [1, 2, 3], ["A", "A", "A"]]
            break
        elif user_choice == 4:
            print("-" * 50)
            list_fav_keys = print_fav_keys()
            for i in range(len(list_fav_keys)):
                print("{} - {}".format(i + 1, list_fav_keys[i]))
            print("-" * 50)
            key = get_favourite_key(list_fav_keys)
            break
    return key


def print_key(key):
    print("This is the key you used to encrypt the message:")
    print("-" * 50)
    plug_amount = len(key[0][0])
    print("Plugboard connections:")
    for i in range(plug_amount):
        print("Letter", key[0][0][i], "is connected to letter", key[0][1][i])
    print("-" * 50)
    print("Rotor order:")
    print("Fast rotor is {}. Medium rotor is {}. Slow rotor is {}".format(key[1][0], key[1][1], key[1][2]))
    print("-" * 50)
    print("Rotor initial positions:")
    print("Fast rotor initial position", key[2][0])
    print("Medium rotor initial position", key[2][1])
    print("Slow rotor initial position", key[2][2])
    print("")


def add_spaces(text, length):
    return ' '.join(text[i:i + length] for i in range(0, len(text), length))


def turn_rotor(rot_pos_indexes_list, double_step_notch):
    f_pos_index = rot_pos_indexes_list[0]
    m_pos_index = rot_pos_indexes_list[1]
    s_pos_index = rot_pos_indexes_list[2]
    f_pos_index = (f_pos_index + 1) % ALPHABET_LENGTH

    if f_pos_index == double_step_notch[0]:
        m_pos_index = (m_pos_index + 1) % ALPHABET_LENGTH
        if m_pos_index == double_step_notch[1]:
            s_pos_index = (s_pos_index + 1) % ALPHABET_LENGTH
    rot_pos_indexes_list = [f_pos_index, m_pos_index, s_pos_index]
    return rot_pos_indexes_list


def print_basic_menu():
    print("1 - Encrypt / decrypt text")
    print("2 - Exit program")


def animation_plugboard(key):
    print("Setting up plugboard connections...")
    time.sleep(1)
    plug_amount = len(key[0][0])
    for i in range(plug_amount):
        print(key[0][0][i], " ", end="", flush=True)
        time.sleep(0.3)
        for k in range(12):
            print("-", end="", flush=True)
            time.sleep(0.1)
        print(" ", key[0][1][i], " ", flush=True)
    print("Done!")
    time.sleep(0.5)


def animation_rotors_choosing(key):
    fast_rotor = key[1][0]
    medium_rotor = key[1][1]
    slow_rotor = key[1][2]
    print("Placing rotors...")
    time.sleep(1)
    print(fast_rotor, " ", end="", flush=True)
    time.sleep(0.5)
    print(medium_rotor, " ", end="", flush=True)
    time.sleep(0.5)
    print(slow_rotor, " ", end="", flush=True)
    time.sleep(0.5)


def animation_rotors_turning(rot_pos_indexes_list):
    print("Turning fast rotor into position...")
    time.sleep(1)
    for i in range(rot_pos_indexes_list[0] + 1):
        print(ENGLISH_ALPHABET[i], 0, 0)
        time.sleep(0.2)
        fast_rotor = ENGLISH_ALPHABET[i]
    print("Turning medium rotor into position...")
    time.sleep(1)
    for j in range(rot_pos_indexes_list[1] + 1):
        print(fast_rotor, ENGLISH_ALPHABET[j], 0)
        time.sleep(0.2)
        medium_rotor = ENGLISH_ALPHABET[j]
    print("Turning slow rotor into position...")
    time.sleep(1)
    for k in range(rot_pos_indexes_list[2] + 1):
        print(fast_rotor, medium_rotor, ENGLISH_ALPHABET[k])
        time.sleep(0.2)
    print("Done!")
    time.sleep(0.5)


if __name__ == '__main__':
    main()
