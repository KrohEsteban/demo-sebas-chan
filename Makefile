PYTHON ?= python3
ARGS ?=
PYFILE ?= hello.py

.PHONY: run check

## run: execute the greeting script (pass flags via ARGS)
run:
	$(PYTHON) $(PYFILE) $(ARGS)

## check: validate Python syntax without writing artifacts
check:
	$(PYTHON) -c "import ast, pathlib, sys; ast.parse(pathlib.Path(sys.argv[1]).read_text(), sys.argv[1])" $(PYFILE)
