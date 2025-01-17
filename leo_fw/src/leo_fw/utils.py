from __future__ import annotations

import sys
from typing import Any


def is_tool(name: str) -> bool:
    """!
    Check whether an executable exists on PATH.
    @param name Name of the executable
    @return True if executable exists, False otherwise
    """
    from whichcraft import which

    return which(name) is not None


def write_flush(msg: str):
    """!Write a message to standard output and flush the buffer"""
    sys.stdout.write(msg)
    sys.stdout.flush()


def query_yes_no(question: str, default: str = "yes") -> bool:
    """!
    Ask a yes/no question via input() and return their answer.
    @param question The question that is presented to the user.
    @param default The presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).
    @return True if the answer is "yes", False otherwise
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError(f"invalid default answer: '{default}'")

    while True:
        write_flush(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' " "(or 'y' or 'n').")


def prompt_options(options: list[tuple[str, Any]], default: int = 1) -> str:
    for i, (name, _) in enumerate(options):
        print(f"{i+1}) {name}")

    while True:
        input_raw = input(f"Your selection [{default}]: ")
        if input_raw == "":
            selected_nr = default - 1
        else:
            selected_nr = int(input_raw) - 1
        if 0 <= selected_nr < len(options):
            _, selected = options[selected_nr]
            return selected
        else:
            print(f"Please select a valid option")
