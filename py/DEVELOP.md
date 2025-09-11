# Development

Instructions for setting up a development environment, running tests, and contributing to the project.

## Dependencies

The following dependencies are required for development:

- make
- Python3.12
- uv
- tox

## Development

This project utilizes `uv` for dependency management, we encourage you to use it as it will make your life easier as it will handle virtual environments and dependency resolution for you.

### Create a virtual environment and install dependencies

   ```bash
   make sync-deps
   ```

This will create a virtual environment in the `.venv` directory and install all the dependencies specified in `pyproject.toml`. 

The virtual environment will be automatically activated when you run `uv` commands. To activate the virtual environment manually, you can use:

```bash
source .venv/bin/activate
```

### Export dependencies to requirements.txt
Dependabot and other security tools often require a `requirements.txt` file to scan for vulnerabilities. You can generate this file from your `uv` lock file using the following command:

```bash
make generate-requirements
```
This will create or update the `requirements.txt` file with the current dependencies.

### Running Tests

To run the tests, you can use `tox`, which will create isolated environments for testing. Simply run:

```bash
make test
```

This will execute the tests on all specified Python versions.

### Type Checking

To perform type checking on the codebase, you can use `mypy`. Run the following command:

```bash
make type-check
```

### Linting and Formatting

To check the code for style issues and potential errors, you can use `ruff`. Run the following command:

```bash
make lint # check code issues
make format # check formatting issues
```
To automatically fix style issues, you can run:
