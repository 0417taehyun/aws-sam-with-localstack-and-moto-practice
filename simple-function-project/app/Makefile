.PHONY: install
install:
	pip install -U poetry && poetry install

.PHONY: update
update:
	poetry update

.PHONY: lint
lint:
	poetry run pre-commit install && poetry run pre-commit run

.PHONY: local-run
local-run:
	poetry run sam local invoke -t ../template.yaml -e ../events/event.json --env-vars ../env.json
