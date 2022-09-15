import pytest
from typer.testing import CliRunner

from cardloop.core import app, get_yaml_frontmatter

runner = CliRunner()


@pytest.mark.parametrize(
    "file_name",
    [
        "Hal Jordan",
        "Picard",
        "/tmp/you-rock.md",
        "/home/you/noooooo.md",
        "Hal Jordan",
        "Picard",
    ],
)
def test_expected_stdout_when_file_does_not_exist(file_name):
    expected_stdout = f"File '{file_name}' does not exist"
    result = runner.invoke(app, ["--file-path", file_name])
    assert result.exit_code == 2
    assert expected_stdout in result.stdout
    not_expected_stdout = f"Processing file '{file_name}' "
    assert not (not_expected_stdout in result.stdout)


@pytest.mark.parametrize(
    "file_name",
    [
        "../etc/samples/2022-04-05-180326-814.md",
        "../etc/samples/2022-04-16-102521-814.md",
    ],
)
def test_expected_stdout_when_file_exists(file_name):
    expected_stdout = ["Processing file", file_name.replace("../", "")]
    result = runner.invoke(app, ["--file-path", file_name])
    assert result.exit_code == 0
    for substring in expected_stdout:
        assert substring in result.stdout


@pytest.mark.parametrize(
    "file_name,expected_keys",
    [
        [
            "../etc/samples/2022-04-05-180326-814.md",
            ["author", "title", "date", "categories", "tags"],
        ],
        [
            "../etc/samples/2022-04-16-102521-814.md",
            ["author", "title", "date", "categories", "tags", "references"],
        ],
    ],
)
def test_get_yaml_frontmatter_keys(file_name, expected_keys):
    frontmatter = get_yaml_frontmatter(file_name)
    assert list(frontmatter.keys()) == expected_keys
