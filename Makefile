PYTHON ?= python3
ARGS ?=
PYFILE ?= hello.py
TEXTCOUNT ?= textcount.py
PYFILES ?= $(PYFILE) $(TEXTCOUNT)

.PHONY: run run-textcount check

## run: execute the greeting script (pass flags via ARGS)
run:
	$(PYTHON) $(PYFILE) $(ARGS)

## run-textcount: execute the text counter (pass flags via ARGS)
run-textcount:
	$(PYTHON) $(TEXTCOUNT) $(ARGS)

## check: validate Python syntax of every script without writing artifacts
check:
	@for f in $(PYFILES); do \
		$(PYTHON) -c "import ast, pathlib, sys; ast.parse(pathlib.Path(sys.argv[1]).read_text(), sys.argv[1])" $$f || exit 1; \
	done
