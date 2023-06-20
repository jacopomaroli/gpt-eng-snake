include .env
export

env:
	pipenv install --python 3.9.0

run:
	pipenv run gpt-engineer . --model gpt-3.5-turbo

game:
	cd workspace; pipenv run python server.py
