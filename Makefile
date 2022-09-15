.PHONY: serve-docs
serve-docs:
	python3 -m http.server --directory=./docs/build/html
