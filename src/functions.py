import os

from logger import *


def find_message_name_with_id(n: int, message_type: str) -> str:
    """
    Get the name of the message (composer/event) corresponding
    :param message_type:
    :param n:
    :return:
    """
    habbo_messages = open("communication/HabboMessages.as", "r")
    content = habbo_messages.readlines()
    for line in content:
        if str([n]) + " = " in line and message_type + ";" in line:
            split_line = line.split("=")
            message_name = split_line[1]
            habbo_messages.close()
            return message_name[1:len(message_name) - 2]
    habbo_messages.close()
    return ""


def display_messages_containing_word(word: str) -> None:
    """
    Display all messages containing the given word
    :param word:
    :return:
    """
    habbo_messages = open("communication/HabboMessages.as", "r")
    content = habbo_messages.readlines()
    for line in content:
        if " = " in line and word in line:
            print_info(line)
    habbo_messages.close()


def get_path_from_habbo_messages(file_name: str) -> str:
    """
    Get file path
    :param file_name:
    :return:
    """
    habbo_messages = open("communication/HabboMessages.as", "r")
    path = ""
    for line in habbo_messages.readlines():
        if "import" in line and file_name in line:
            split_line = line.split("habbo.")
            path = split_line[-1]
            path = path[0:len(path) - 2]
            path = path.replace(".", "/") + ".as"
    habbo_messages.close()
    return path


def display_message_structure(n: int, message_type: str) -> None:
    """
    Display the entire packet class
    :param message_type:
    :param n: message composer id
    :return:
    """
    message_name = find_message_name_with_id(n, message_type)
    if message_name != "":
        if message_type == "Event":
            # get path (incoming)
            path = get_path_from_habbo_messages(message_name)
            # open file
            if path != "":
                message_event = open(path, "r")
                print_file_content(message_event.read())
                message_event.close()

                # get path (parser)
                path = path.replace("incoming", "parser").replace("Event", "Parser")

                try:
                    message_parser = open(path, "r")
                    print_file_content(message_parser.read())
                    message_parser.close()
                except FileNotFoundError:
                    print_error("File not found!")
            else:
                print_error("No message event found.")
        elif message_type == "Composer":
            # get path
            path = get_path_from_habbo_messages(message_name)
            # open file
            if path != "":
                try:
                    message_composer = open(path, "r")
                    print_file_content(message_composer.read())
                    message_composer.close()
                except FileNotFoundError:
                    print_error("File not found!")
            else:
                print_error("No message composer found.")
        else:
            pass
    else:
        print_error("No message found with this name.")


def display_folder_content(path: str) -> None:
    """
    Display folder and file names
    :param path:
    :return:
    """
    print("Folders:")
    try:
        contents = os.listdir(path)
        for content in contents:
            if os.path.isdir(os.path.join(path, content)):
                print("/" + content + "/")

        print("\nFiles:")
        for content in contents:
            if not os.path.isdir(os.path.join(path, content)):
                print("/" + content)
    except FileNotFoundError:
        print_error("The specified path was not found")
