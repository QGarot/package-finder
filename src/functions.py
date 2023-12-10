def find_message_composer_with_id(n: int) -> str:
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
            return message_composer_name[1:len(message_composer_name) - 2]
    return ""
