from logger import *
from functions import *
import os
from platform import system
from actions import *


def run() -> None:
    launched = True
    path = ""
    while launched:
        print_info("What do you want to do?")
        print("- Find message composer " + FIND_COMPOSER)
        print("- Find message event " + FIND_EVENT)
        print("- Search a message with specific word " + FIND_MESSAGE)
        print("- Clear console " + RESET_TERMINAL)
        print("- Give folder content " + LIST_FOLDER_CONTENT)
        print("- Reset path " + RESET_PATH)
        print("- Display file content " + OPEN_FILE)
        print("- Cancel " + CANCEL)

        resp = input("<< ")

        if resp == CANCEL:
            launched = False
        elif resp == FIND_COMPOSER:
            print_info("Give the packet id")
            n = int(input("<< "))
            display_message_structure(n, "Composer")
        elif resp == FIND_EVENT:
            print_info("Give the packet id")
            n = int(input("<< "))
            display_message_structure(n, "Event")
        elif resp == RESET_TERMINAL:
            current_os = system()
            if current_os == "Windows":
                clear_console = lambda: os.system('cls')
            else:
                clear_console = lambda: os.system('clear')
            clear_console()
        elif resp == FIND_MESSAGE:
            print_info("What word do you want to use to search your package?")
            word = str(input("<< "))
            display_messages_containing_word(word)
        elif resp == LIST_FOLDER_CONTENT:
            print_info("You are in: " + path)
            print_info("From which folder do you want to list the files in? ")
            folder_name = str(input("<< "))
            folder_name = folder_name.replace(".", "/")
            path = path + folder_name + "/"
            display_folder_content(path)
        elif resp == RESET_PATH:
            path = ""
            print_info("Path updated")
        elif resp == OPEN_FILE:
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
