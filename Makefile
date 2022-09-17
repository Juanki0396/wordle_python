## -----------------
## -----------------
## Config Variables
## -----------------
## -----------------

# Project
PROJECT_NAME = wordle_python

# Python
PYTHON_VERSION = python3.10

# Venv
VENV_NAME = .venv
VENV_ACTIVATE = $(VENV_NAME)/bin/activate

# Packaging
PACKAGE_TOOL = flit
PACKAGE_BUILD = $(PACKAGE_TOOL) build
PACKAGE_INSTALL = $(PACKAGE_TOOL) install
PACKAGE_DEPENDENCIES = dev-requirements.txt


## -----------------
## -----------------
## Recipes
## -----------------
## -----------------

SHELL := /bin/bash
.PHONY: venv clean_venv compile_dev_dependencies install build
.SILENT: clean_venv

venv: # Install the virtual environment
	@echo "Creating the virtual enviroment"
	$(PYTHON_VERSION) -m venv $(VENV_NAME)
	source $(VENV_ACTIVATE) && pip install --upgrade pip && pip install pip-tools
	source $(VENV_ACTIVATE) && pip-sync $(PACKAGE_DEPENDENCIES)

clean_venv: # Clean the venv folder
	@echo "Deleting the environment"
	rm -r $(VENV_NAME)

compile_dev_dependencies: # Compiling dev requeriments file
	@echo "Compiling developing dependencies"
	$(VENV_ACTIVATE) && pip-compile -o $(PACKAGE_DEPENDENCIES) --extra dev pyproject.toml

install: # Install the package
	@echo "Installing the package: $(PROJECT_NAME)"
	$(PACKAGE_INSTALL)

build: # build the package
	@echo "Building the package: $(PROJECT_NAME)"
	$(PACKAGE_BUILD)