############################################################################
## Defaults
############################################################################
uv=`which uv`


#***********************************
### Export uv.lock to requirements.txt. For security scanning purposes. Read DEVELOP.md for details
#***********************************
.PHONY : generate-requirements
generate-requirements:
	@echo ">generating requirements.txt"
	$(uv) export --output-file 'requirements.txt'


#***********************************
### Compile deps from pyproject.toml to uv.lock
#***********************************
.PHONY : compile-deps
compile-deps:
	@echo ">compiling python dependencies"
	$(uv) lock && \
	[ ! -f local-requirements.in ] || \
	($(uv) export -o cons-requirements.txt && \
	$(uv) pip compile --generate-hashes 'local-requirements.in' -o 'local-requirements.txt'; \
	rm cons-requirements.txt)


#***********************************
### Sync local venv to match uv.lock
#***********************************
.PHONY : sync-deps
sync-deps:
	@echo ">synchronizing python dependencies in local venv"
	$(uv) sync --locked

#***********************************
### Lint/security check with ruff
#***********************************
.PHONY : lint
lint:
	@echo ">running lint"
	$(uv) run tox -e ruff-check


#***********************************
### Autoformat with ruff
#***********************************
.PHONY : format
format:
	@echo ">running formatting"
	$(uv) run tox -e ruff-format


#***********************************
### Static typecheck with mypy
#***********************************
.PHONY : typecheck
typecheck:
	@echo ">running mypy"
	$(uv) run tox -e mypy


#***********************************
### tox test
#***********************************
.PHONY : test
test: testunit
tests: testunit
testunit:
	$(uv) run tox
