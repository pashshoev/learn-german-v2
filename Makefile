.PHONY: run install update-deps


install:
	pip install -r deps/requirements.txt

update-deps:
	pip install pip-tools
	pip-compile deps/requirements.in --output-file=deps/requirements.txt

run:
	python app/main.py

