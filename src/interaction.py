from src.logger import *
from src.functions import *
import os

cancel = ":q"
find_composer = ":c"
find_event = ":e"
reset_terminal = ":r"
find_message = ":m"
list_folder_content = ":l"
reset_path = ":rp"
open_file = ":o"


def run() -> None:
    launched = True
    path = ""
    while launched:
        print_info("What do you want to do?")
        resp = input("<< ")

        if resp == cancel:
            launched = False
        elif resp == find_composer:
            print_info("Give the packet id")
            n = int(input("<< "))
            display_message_structure(n, "Composer")
        elif resp == find_event:
            print_info("Give the packet id")
            n = int(input("<< "))
            display_message_structure(n, "Event")
        elif resp == reset_terminal:
            clear_console = lambda: os.system('cls')
            clear_console()
        elif resp == find_message:
            print_info("What word do you want to use to search your package?")
            word = str(input("<< "))
            display_messages_containing_name(word)
        elif resp == list_folder_content:
            print_info("You are in: " + path)
            print_info("From which folder do you want to list the files in? ")
            folder_name = str(input("<< "))
            folder_name = folder_name.replace(".", "/")
            path = path + folder_name + "/"
            display_folder_content(path)
        elif resp == reset_path:
            path = ""
            print_info("Path updated")
        elif resp == open_file:
            print_info("File name: ")
            file_name = str(input("<< "))
            try:
                message_composer = open(path + file_name, "r")
                print_file_content(message_composer.read())
                message_composer.close()
            except FileNotFoundError:
                print_error("File not found!")
        else:
            pass
