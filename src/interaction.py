from src.logger import *
from src.functions import *
import os

cancel = ":q"
find_composer = ":c"
find_event = ":e"
reset_terminal = ":r"
find_message = ":m"


def run() -> None:
    launched = True
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
        else:
            pass
