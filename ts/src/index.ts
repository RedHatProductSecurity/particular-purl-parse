import { PackageURL } from 'packageurl-js';

export function psComponentFromPurl(purl: string) {
  const parsedPurl = PackageURL.fromString(purl);
  if (parsedPurl.type === 'oci') {
    return psComponentOCI(parsedPurl);
  } else if (parsedPurl?.qualifiers?.['rpmmod']) {
    return `${parsedPurl?.qualifiers?.['rpmmod']}/${parsedPurl.name}`;
  } else {
    return parsedPurl.name;
  }
}

function psComponentOCI(parsedPurl: PackageURL) {
  const prefix = parsedPurl?.qualifiers?.['repository_url']?.split('/')[1];
    if (prefix) {
      return `${prefix}/${parsedPurl.name}`;
    } else {
      throw new Error('Invalid repository_url in OCI PURL');
    }
}

export * from 'packageurl-js';