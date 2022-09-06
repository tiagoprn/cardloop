#!/usr/bin/env python3

"""
TODO: Edit here with a good description of what does this script do.

TODO: Provide an example to how to use it with its parameters. E.g.:
    python3 core.py <name>
"""

import logging
import os
import sys
from pathlib import Path

import typer

app = typer.Typer()


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
        logging.StreamHandler(sys.stdout),
    ],
)


@app.command()
def process_file(file_path: Path):
    if not file_path.is_file():
        raise FileNotFoundError(
            f"Not a file, or file does not exist: '{file_path}'"
        )

    print(f"Ready to process file '{file_path}'...")


if __name__ == "__main__":
    app()
