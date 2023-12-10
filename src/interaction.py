from src.logger import *
from src.functions import *
import os

cancel = ":q"
find_composer = ":c"
find_event = ":e"
reset = ":r"


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
        elif resp == reset:
            clear_console = lambda: os.system('cls')
            clear_console()
        else:
            pass
