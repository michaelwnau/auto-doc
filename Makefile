PYTHON := python3
PYTEST := pytest
UNITTEST := $(PYTHON) -m unittest
DOCTEST := $(PYTHON) -m doctest

.PHONY: test unittest doctest init clean

test: unittest doctest

unittest:
	@echo "Running unittests..."
	$(UNITTEST) discover

doctest:
	@echo "Running doctests..."
	$(DOCTEST) -v **/*.py

init:
	@echo "Setting up project scaffolding..."
	$(PYTHON) -m venv venv
	. venv/bin/activate
	pip install --upgrade pip
	pip install pytest

clean:
	@echo "Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +


# Run all tests: `make test`
# Run unittests only: `make unittest`
# Run doctests only: `make doctest`
# Initialize the project: `make init`
# Clean up temporary files: `make clean`