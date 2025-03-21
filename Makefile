.PHONY: install test lint format clean build publish

install:
	pip install -e ".[dev]"

test:
	pytest

coverage:
	pytest --cov=ethanpolars --cov-report=term --cov-report=html

lint:
	ruff check src tests examples
	mypy src

format:
	black src tests examples
	isort src tests examples

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf htmlcov/
	rm -rf .coverage
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.pyd" -delete

build: clean
	python -m build

publish: build
	twine upload dist/*
