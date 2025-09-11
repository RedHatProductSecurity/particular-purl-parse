# Particular PURL Parse - Python Package

A Python library for parsing PackageURL (PURL) strings and extracting component information.

## Installation

```bash
pip install particular-purl-parse
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

See [DEVELOP.md](DEVELOP.md) for details on setting up a development environment, running tests, and contributing to the project.
