#!/usr/bin/env python3

"""
TODO: Edit here with a good description of what does this script do.

TODO: Provide an example to how to use it with its parameters. E.g.:
    python3 sample_script.py <name>
"""

import argparse
import logging
import os
from datetime import datetime

CURRENT_SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]
LOG_FORMAT = (
    "[%(asctime)s PID %(process)s "
    "%(filename)s:%(lineno)s - %(funcName)s()] "
    "%(levelname)s -> \n"
    "%(message)s\n"
)
logging.basicConfig(
    format=LOG_FORMAT,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(f"{CURRENT_SCRIPT_NAME}.log"),
        # logging.StreamHandler(stdout)
    ],
)


def greet(name: str) -> str:
    now = datetime.now()

    if now.hour >= 18 or now.hour < 6:
        time = "night"
    elif now.hour >= 6 and now.hour < 12:
        time = "morning"
    elif now.hour >= 12 and now.hour < 18:
        time = "afternoon"

    return f"Hello {name}! Have a good {time}!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help="type the person name here")
    parsed_arguments = parser.parse_args()
    message = greet(parsed_arguments.name)
    print(message)
