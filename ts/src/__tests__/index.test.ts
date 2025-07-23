import { psComponentFromPurl } from '../index';

describe('psComponentFromPurl', () => {
  it('should extract component name from OCI PURL', () => {
    const purl = 'pkg:oci/nginx@1.21.0?repository_url=docker.io/library';
    const result = psComponentFromPurl(purl);
    expect(result).toBe('library/nginx');
  });

  it('should extract component name from RPM PURL with rpmmod', () => {
    const purl = 'pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx';
    const result = psComponentFromPurl(purl);
    expect(result).toBe('nginx/nginx');
  });

  it('should extract component name from regular PURL', () => {
    const purl = 'pkg:npm/lodash@4.17.21';
    const result = psComponentFromPurl(purl);
    expect(result).toBe('lodash');
  });

  it('should throw error for OCI PURL without repository_url', () => {
    const purl = 'pkg:oci/nginx@1.21.0';
    expect(() => {
      psComponentFromPurl(purl);
    }).toThrow('Invalid repository_url in OCI PURL');
  });

  it('should throw error for OCI PURL with invalid repository_url', () => {
    const purl = 'pkg:oci/nginx@1.21.0?repository_url=invalid';
    expect(() => {
      psComponentFromPurl(purl);
    }).toThrow('Invalid repository_url in OCI PURL');
  });
}); 