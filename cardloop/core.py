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

import frontmatter
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


def get_yaml_frontmatter(file_path: Path) -> dict:
    with open(file_path, "r", encoding="utf-8") as input_file:
        return frontmatter.load(input_file)


@app.command()
def process_file(
    file_path: Path = typer.Option(
        default=None,
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
    )
):
    print(f"Processing file '{file_path}'...")


if __name__ == "__main__":
    app()
