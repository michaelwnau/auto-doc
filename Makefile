PYTHON := python3
PYTEST := pytest
UNITTEST := $(PYTHON) -m unittest
DOCTEST := $(PYTHON) -m doctest
COVERAGE := coverage
FLAKE8 := flake8

.PHONY: test unittest doctest coverage flake8 init clean

test: unittest doctest

unittest:
	@echo "Running unittests..."
	$(UNITTEST) discover

doctest:
	@echo "Running doctests..."
	$(DOCTEST) -v **/*.py

coverage:
	@echo "Running coverage..."
	$(COVERAGE) run --source=. -m pytest
	$(COVERAGE) report

flake8:
	@echo "Running flake8..."
	$(FLAKE8) --ignore=E501,W503 .

init:
	@echo "Setting up project scaffolding..."
	$(PYTHON) -m venv venv
	. venv/bin/activate
	pip install --upgrade pip
	pip install pytest coverage flake8

clean:
	@echo "Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +


# To use from terminal
# Run all tests: $ `make test`
# Run unittests only: $ `make unittest`
# Run doctests only: $ `make doctest`
# Measure code coverage: $ `make coverage`
# Check code style and syntax: $ `make flake8`
# Initialize the project: $ `make init`
# Clean up temporary files: $ `make clean`