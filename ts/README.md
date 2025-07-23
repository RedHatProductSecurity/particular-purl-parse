# Particular PURL Parse - TypeScript Package

A TypeScript/JavaScript library for parsing PackageURL (PURL) strings and extracting component information.

## Installation

### From GitHub Packages

```bash
npm install @redhat-product-security/particular-purl-parse
```

### From Source

```bash
git clone https://github.com/RedHatProductSecurity/particular-purl-parse.git
cd particular-purl-parse/ts
npm install
npm run build
```

## Usage

### TypeScript

```typescript
import { psComponentFromPurl } from '@redhat-product-security/particular-purl-parse';

// Example usage
const component = psComponentFromPurl("pkg:oci/nginx@1.21.0?repository_url=docker.io/library");
console.log(component); // Output: library/nginx

// With RPM module
const component2 = psComponentFromPurl("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx");
console.log(component2); // Output: nginx/nginx

// Regular PURL
const component3 = psComponentFromPurl("pkg:npm/lodash@4.17.21");
console.log(component3); // Output: lodash
```

### JavaScript

```javascript
const { psComponentFromPurl } = require('@redhat-product-security/particular-purl-parse');

// Example usage
const component = psComponentFromPurl("pkg:oci/nginx@1.21.0?repository_url=docker.io/library");
console.log(component); // Output: library/nginx
```

## Development

### Setup

1. Install dependencies:
```bash
npm install
```

2. Build the project:
```bash
npm run build
```

### Testing

```bash
# Run tests
npm test

# Run tests with coverage
npm run test -- --coverage

# Run tests in watch mode
npm run test -- --watch
```

### Building

```bash
# Build for production
npm run build

# Build in watch mode
npm run dev
```

### Code Quality

```bash
# Lint code
npm run lint

# Format code
npm run format
```

## Features

- **OCI PURL Support**: Extracts component names from OCI package URLs using repository_url qualifier
- **RPM Module Support**: Handles RPM packages with rpmmod qualifier
- **Standard PURL Support**: Works with regular PackageURL strings
- **Error Handling**: Comprehensive error handling for invalid PURLs
- **Type Safety**: Full TypeScript support with type definitions
- **ES Modules**: Support for both CommonJS and ES modules

## Dependencies

- `packageurl-js>=1.0.0` - For PackageURL parsing functionality

## License

MIT License - see LICENSE file for details. 