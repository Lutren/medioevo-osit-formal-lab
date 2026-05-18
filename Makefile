.PHONY: install test lint format typecheck ci

install:
	pip install -e ".[dev]"

test:
	pytest -q

lint:
	ruff check src tests

format:
	ruff format src tests

typecheck:
	mypy src

ci: lint typecheck test

