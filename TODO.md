# Checklist

- [-] Draft the code to process a markdown file with the corresponding unit tests (focus on the happy path)
    - [x] get the yaml frontmatter
    - [-] validate the yaml frontmatter (using pydantic)
	- [x] install pydantic
	- [ ] code the validation
    - [ ] parse the body of the markdown file (extract each block of question-answer)

- [ ] Use cases - document each step below on a markdown file under `docs/` with a README.md as the index - use mermaid where applicable:
    - [ ] draft the use cases
    - [ ] draft the database schema
    - [ ] implement sqlite persistance (through a wrapper like "SQLModel" or "records")
    - [ ] code the use cases

- [ ] fix: check why `make coverage` is failing when `make test` is passing.

- [ ] refactor to classes.

- [ ] error handling (not so happy path ;)

- [ ] Add CLI screenrecord of the functionality (using OBS, convert to a gif file after finished)

- [ ] After finishing, post on "r/PKMS" subreddit and others (LinkedIn, Twitter, ProductHunt etc...) - there may be more people interested to collect feedback from there.

- [x] Add sample markdown files to <etc/samples>

- [x] Add LICENSE

- [x] [lib for yaml frontmatter](https://github.com/eyeseast/python-frontmatter)

- [x] Fix .pylintrc. After finishing, copy to </storage/src/minimum-viable-python-script>.

- [x] Create a local git repo `cardloop` based on [my cookiecutter minimum-viable-python-script](https://github.com/tiagoprn/minimum-viable-python-script).
    - [x] Description: 'Reads markdown files with a yaml frontmatter and with questions and answers, to use as a simple CLI spaced repetition program ("anki-like").'

- [x] Improvements to </storage/src/minimum-viable-python-script> (separated branch):
	- [x] python version
	- [x] README.md
	- [x] Write a generic function with test cases to be an example.
