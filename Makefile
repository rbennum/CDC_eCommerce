# Default values (can be overridden)
CUSTOMERS ?= 1
PRODUCTS ?= 1
ORDERS ?= 1

# Virtual environment directory
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.PHONY: create-tables
create-tables:
	$(PYTHON) main.py --create-tables

.PHONY: drop-tables
drop-tables:
	$(PYTHON) main.py --drop-tables

.PHONY: gen-customers
gen-customers:
	$(PYTHON) main.py --gen-customers $(CUSTOMERS)

.PHONY: gen-products
gen-products:
	$(PYTHON) main.py --gen-products $(PRODUCTS)

.PHONY: gen-orders
gen-orders:
	$(PYTHON) main.py --gen-orders $(ORDERS)

.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV)

.PHONY: install
install: venv
	$(PIP) install -r requirements.txt
