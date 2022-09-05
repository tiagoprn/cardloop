# from datetime import datetime

import pytest
import time_machine

from cardloop.core import greet


@pytest.mark.parametrize(
    "name,fake_current_datetime,time",
    [
        ["Hal Jordan", "2021-01-01 05:59", "night"],
        ["Hal Jordan", "2021-01-01 06:00", "morning"],
        ["Hal Jordan", "2021-01-01 11:59", "morning"],
        ["Hal Jordan", "2021-01-01 12:00", "afternoon"],
        ["Hal Jordan", "2021-01-01 17:59", "afternoon"],
        ["Hal Jordan", "2021-01-01 18:00", "night"],
        ["Hal Jordan", "2021-01-01 18:01", "night"],
        ["Hal Jordan", "2021-01-01 23:59", "night"],
        ["Hal Jordan", "2021-01-01 00:00", "night"],
    ],
)
def test_greet(name, fake_current_datetime, time):
    with time_machine.travel(fake_current_datetime, tick=False):
        result = greet(name)
        expected_result = f"Hello {name}! Have a good {time}!"
        assert result == expected_result
