# cardloop

Reads markdown files with a yaml frontmatter and with questions and answers, to use as a simple CLI spaced repetition program ("anki-like").

## Setting up the development environment

1. Make sure you have pyenv installed. If not, install it.

2. Install pipx on your python distribution. (e.g. Ubuntu):

`$ sudo apt install pipx`

With pipx you can install python utilities on isolated environments, which fits perfectly to install poetry.

3. After installing pipx, run: `pipx install poetry`

4. Create and enter a folder with the project's name, where you will use pyenv to define the python version that will be used by poetry to automatically create the virtualenv:
```bash
pyenv local 3.10.4
```

5. If you have already cloned this repository or just created this repository from [minimum-viable-python-script cookiecutter](https://github.com/tiagoprn/minimum-viable-python-script), ignore this. Otherwise:
A. Clone this repository with git clone
B. Enter the cloned repository folder

6. Run the following commands to setup the development environment:

```bash
make shell
make requirements
make style  # this will fix any style issues that may happen if e.g. your script name is too big or small
```

7. To validate the development environment is working, run the commands below:

```bash
$ make style-check
$ make lint
$ make test
$ make run
```

Type `make` on the project folder to get a description of each one of the make commands above, and to see other ones available.

8. If you have just cloned this repository or if it is already on version control, ignore this step. If you have just created this repository from [minimum-viable-python-script cookiecutter](https://github.com/tiagoprn/minimum-viable-python-script), now you can bootstrap version control on this repository to do your first commit and start coding your project:

```bash
$ git init
$ git add .
$ git commit -m 'feat: boostrapping project from cookiecutter'
```


# Notes

- To supress "Entering Directory" messages when running make commands, run the command with `make -s` ("-s" means "silent"). e.g.: `make -s run`

- To understand a little more about poetry, you can check [this note on my site](https://writeloop.dev/posts/2022-05-05-085202-814/).

