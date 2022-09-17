.PHONY: docs
docs:
	poetry run sphinx-apidoc --output-dir ./docs/source ./muos
	poetry run make --directory=./docs html

.PHONY: serve-docs
serve-docs:
	python3 -m http.server --directory=./docs/build/html

.PHONY: test
test:
	poetry run pytest --codecov --cov=./muos ./tests
