# Makefile for Count-Min Sketch project

.PHONY: help build build-dev example install publish clean

# Default target
help:
	@echo "Available targets:"
	@echo "  build      - Build the project (Release mode with tests)"
	@echo "  build-dev  - Build the project in development mode"
	@echo "  example    - Run the C++ example"
	@echo "  install    - Install the package locally"
	@echo "  publish    - Publish to PyPI"
	@echo "  clean      - Clean build artifacts"
	@echo ""
	@echo "Usage: make <target>"

# Build targets
build:
	@./scripts/build.sh

build-dev:
	@./scripts/build-dev.sh

# Example target
example: build
	@cd build && ./cmsketch_example

# Install target
install: build
	@uv pip install -e .

# Publish target
publish:
	@./scripts/publish.sh

# Clean target
clean:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
