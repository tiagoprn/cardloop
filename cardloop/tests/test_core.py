from pathlib import Path

import pytest

from cardloop.core import process_file


@pytest.mark.parametrize(
    "file_name, expected_exception_type",
    [
        ["Hal Jordan", AttributeError],
        ["Picard", AttributeError],
        [Path("/tmp/you-rock.md"), FileNotFoundError],
        [Path("/home/you/noooooo.md"), FileNotFoundError],
        [Path("Hal Jordan"), FileNotFoundError],
        [Path("Picard"), FileNotFoundError],
    ],
)
def test_process_file_when_file_does_not_exist(
    file_name, expected_exception_type
):
    with pytest.raises(expected_exception_type):
        process_file(file_name)
