# Particular PURL Parse - Python Package

A Python library for parsing PackageURL (PURL) strings and extracting component information.

## Installation

### From GitHub Packages

```bash
pip install particular-purl-parse
```

### From Source

```bash
git clone https://github.com/RedHatProductSecurity/particular-purl-parse.git
cd particular-purl-parse/py
pip install -e .
```

## Usage

```python
from particular_purl_parse import ps_component_from_purl

# Example usage
component = ps_component_from_purl("pkg:oci/nginx@1.21.0?repository_url=docker.io/library")
print(component)  # Output: library/nginx

# With RPM module
component = ps_component_from_purl("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx")
print(component)  # Output: nginx/nginx

# Regular PURL
component = ps_component_from_purl("pkg:npm/lodash@4.17.21")
print(component)  # Output: lodash
```

## Development

### Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install in development mode:
```bash
pip install -e ".[dev]"
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=particular_purl_parse

# Run specific test file
pytest tests/test_core.py

# Run with verbose output
pytest -v
```

### Building

```bash
# Build package
python -m build

# Install from built package
pip install dist/*.whl
```

## Features

- **OCI PURL Support**: Extracts component names from OCI package URLs using repository_url qualifier
- **RPM Module Support**: Handles RPM packages with rpmmod qualifier
- **Standard PURL Support**: Works with regular PackageURL strings
- **Error Handling**: Comprehensive error handling for invalid PURLs
- **Type Hints**: Full type annotation support

## Dependencies

- `packageurl-python>=0.11.0` - For PackageURL parsing functionality

## License

MIT License - see LICENSE file for details. 