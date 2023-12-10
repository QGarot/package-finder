def find_message_composer_name_with_id(n: int) -> str:
    """
    Get the name of the message composer corresponding
    :param n:
    :return:
    """
    habbo_messages = open("communication/HabboMessages.as", "r")
    content = habbo_messages.readlines()
    for line in content:
        if str([n]) + " = " in line and "Composer;" in line:
            split_line = line.split("=")
            message_composer_name = split_line[1]
            habbo_messages.close()
            return message_composer_name[1:len(message_composer_name) - 2]
    habbo_messages.close()
    return ""


def display_message_composer_structure(n: int) -> None:
    """

    :param n: message composer id
    :return:
    """
    message_composer_name = find_message_composer_name_with_id(n)
    if message_composer_name != "":
        # get file path
        habbo_messages = open("communication/HabboMessages.as", "r")
        path = ""
        for line in habbo_messages.readlines():
            if "import" in line and message_composer_name in line:
                split_line = line.split(" ")
                path = split_line[-1]
                path = path[17:len(path)-2]
                path = path.replace(".", "/") + ".as"
                print(path)
        habbo_messages.close()

        # open file
        if path != "":
            message_composer = open(path, "r")
            print("-------------------------------------------------------------")
            print(message_composer.read())
            print("-------------------------------------------------------------")
            message_composer.close()
