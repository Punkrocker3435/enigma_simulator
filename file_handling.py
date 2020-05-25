import re


def add_used_text(text):
    with open("used_text.txt", "w") as f:
        f.write(text)


def add_used_key(key):
    with open("used_key.txt", "w") as f:
        f.write(str(key))


def add_favourite_text(text):
    file_text_read = []
    while True:
        user_choice = input("Do you want to add this text to your favourites? (Y/N): ")
        if user_choice == "y" or user_choice == "Y":
            with open("favourite_text.txt", "r") as fr:
                while True:
                    # read next line
                    line = fr.readline()
                    file_text_read.append(line.strip())
                    # if line is empty, you are done with all lines in the file
                    if not line:
                        break
                if text not in file_text_read:
                    with open("favourite_text.txt", "a") as fa:
                        fa.write("\n")
                        fa.write(text)
                    print("Text was successfully added to the favourites list.")
                    print("")
                else:
                    print("Text was already in the list. Nothing has changed.")
                    print("")
                    break
            break
        elif user_choice == "n" or user_choice == "N":
            break
        else:
            print("Sorry, your input was invalid. Please, try again.")
            continue


def add_favourite_key(key):
    str_key = str(key)
    file_key_read = []
    while True:
        user_choice = input("Do you want to add this key to your favourites? (Y/N): ")
        if user_choice == "y" or user_choice == "Y":
            with open("favourite_key.txt", "r") as fr:
                while True:
                    # read next line
                    line = fr.readline()
                    file_key_read.append(line.strip())
                    # if line is empty, you are done with all lines in the file
                    if not line:
                        break
                if str_key not in file_key_read:
                    with open("favourite_key.txt", "a") as fa:
                        fa.write("\n")
                        fa.write(str_key)
                    print("Key was successfully added to the favourites list.")
                    print("")
                else:
                    print("Key was already in the list. Nothing has changed.")
                    print("")
                    break
            break
        elif user_choice == "n" or user_choice == "N":
            break
        else:
            print("Sorry, your input was invalid. Please, try again.")
            continue


def clear_used_text():
    with open("used_text.txt", "w") as f:
        f.write("")


def clear_used_key():
    with open("used_key.txt", "w") as f:
        f.write("")


def get_favourite_text(list_fav_texts):
    while True:
        choice = int(input("Which one do you want to use? Enter its number: "))
        if 0 < choice <= len(list_fav_texts):
            text = list_fav_texts[choice - 1]
            break
        else:
            print("Sorry, your choice was invalid. Please, try again.")
            continue
    return text


def get_favourite_key(list_fav_keys):
    while True:
        choice = int(input("Which one do you want to use? Enter its number: "))
        if 0 < choice <= len(list_fav_keys):
            fav_key = list_fav_keys[choice - 1]
            conns = ""
            fav_key = re.sub("[\W]+", "", fav_key)
            rotor_pos = fav_key[-3] + fav_key[-2] + fav_key[-1]
            rotor_order = fav_key[-6:-3]
            fav_key_list = list(fav_key)
            for i in range(6):
                fav_key_list.pop()
            for char in fav_key_list:
                conns = conns + char
            half = len(conns) // 2
            conn_left = conns[0:half]
            conn_right = conns[0 - half:-1] + conns[-1]
            connections = [list(conn_left), list(conn_right)]
            order = list(rotor_order)
            order_1 = int(order[0])
            order_2 = int(order[1])
            order_3 = int(order[2])
            order = [order_1, order_2, order_3]
            positions = list(rotor_pos)
            key = [connections, order, positions]
            break
        else:
            print("Sorry, your choice was invalid. Please, try again.")
            continue
    return key


def print_fav_text():
    list_fav_texts = []
    with open("favourite_text.txt", "r") as f:
        for line in f:
            list_fav_texts.append(line.strip())
    return list_fav_texts


def print_fav_keys():
    list_fav_keys = []
    with open("favourite_key.txt", "r") as f:
        for line in f:
            list_fav_keys.append(line.strip())
    return list_fav_keys
