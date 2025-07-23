# Particular PURL Parse

A library for parsing PackageURL (PURL) strings and extracting component information. Available for both Python and TypeScript/JavaScript.

This repository contains two separate packages:

- **Python Package** (`py/`) - Python implementation
- **TypeScript Package** (`ts/`) - TypeScript/JavaScript implementation

## Quick Start

### Python

```bash
cd py
pip install -e .
python -c "from particular_purl_parse import ps_component_from_purl; print(ps_component_from_purl('pkg:npm/lodash@4.17.21'))"
```

### TypeScript

```bash
cd ts
npm install
npm run build
node -e "const { psComponentFromPurl } = require('./dist/index.js'); console.log(psComponentFromPurl('pkg:npm/lodash@4.17.21'))"
```

## Installation

### Python Package

```bash
pip install particular-purl-parse
```

### TypeScript/JavaScript Package

```bash
npm install @redhat-product-security/particular-purl-parse
```

## Usage Examples

### Python

```python
from particular_purl_parse import ps_component_from_purl

# OCI PURL
component = ps_component_from_purl("pkg:oci/nginx@1.21.0?repository_url=docker.io/library")
print(component)  # Output: library/nginx

# RPM PURL with rpmmod
component = ps_component_from_purl("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx")
print(component)  # Output: nginx/nginx

# Regular PURL
component = ps_component_from_purl("pkg:npm/lodash@4.17.21")
print(component)  # Output: lodash
```

### TypeScript/JavaScript

```typescript
import { psComponentFromPurl } from '@redhat-product-security/particular-purl-parse';

// OCI PURL
const component = psComponentFromPurl("pkg:oci/nginx@1.21.0?repository_url=docker.io/library");
console.log(component); // Output: library/nginx

// RPM PURL with rpmmod
const component2 = psComponentFromPurl("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx");
console.log(component2); // Output: nginx/nginx

// Regular PURL
const component3 = psComponentFromPurl("pkg:npm/lodash@4.17.21");
console.log(component3); // Output: lodash
```

## Development

### Python Development

```bash
cd py
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
pytest
```

### TypeScript Development

```bash
cd ts
npm install
npm test
npm run build
```

## Features

- **OCI PURL Support**: Extracts component names from OCI package URLs using repository_url qualifier
- **RPM Module Support**: Handles RPM packages with rpmmod qualifier
- **Standard PURL Support**: Works with regular PackageURL strings
- **Error Handling**: Comprehensive error handling for invalid PURLs
- **Type Safety**: Full TypeScript support with type definitions
- **Cross-Platform**: Available for both Python and TypeScript/JavaScript

## Package Structure

```
particular-purl-parse/
├── py/                     # Python implementation
│   ├── particular_purl_parse/
│   ├── tests/
│   ├── setup.py
│   ├── pyproject.toml
│   └── README.md
├── ts/                     # TypeScript implementation
│   ├── src/
│   ├── dist/
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
├── .github/                # GitHub Actions workflows
└── README.md              # This file
```

## Dependencies

### Python
- `packageurl-python>=0.11.0` - For PackageURL parsing functionality

### TypeScript/JavaScript
- `packageurl-js>=1.0.0` - For PackageURL parsing functionality

## License

MIT License - see LICENSE file for details.
