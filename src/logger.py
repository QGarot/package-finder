separator = "-" * 100


def print_error(msg: str) -> None:
    print(">> [Error] " + msg)


def print_file_content(content: str) -> None:
    print(separator)
    print(content)
    print(separator)


def print_info(msg: str) -> None:
    print(">> " + msg)
