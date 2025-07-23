"""
Core functionality for PURL parsing and component extraction.
"""

from packageurl import PackageURL


def ps_component_from_purl(purl: str) -> str:
    """Extract component name from PackageURL string.
    
    Args:
        purl: PackageURL string to parse
        
    Returns:
        Component name string
        
    Raises:
        ValueError: If the PURL is invalid or missing required qualifiers
    """
    if not purl or not isinstance(purl, str):
        raise ValueError('PURL must be a non-empty string')
    
    try:
        parsed_purl = PackageURL.from_string(purl)
    except Exception as e:
        raise ValueError(f'Invalid PURL format: {e}')
    
    if parsed_purl.type == 'oci':
        return _ps_component_oci(parsed_purl)
    
    rpmmod = parsed_purl.qualifiers.get('rpmmod')
    if rpmmod:
        return f"{rpmmod}/{parsed_purl.name}"
    
    return parsed_purl.name


def _ps_component_oci(parsed_purl: PackageURL) -> str:
    """Handle OCI type PackageURL component extraction.
    
    Args:
        parsed_purl: Parsed PackageURL object
        
    Returns:
        Component name for OCI type
        
    Raises:
        ValueError: If repository_url is missing or invalid
    """
    repository_url = parsed_purl.qualifiers.get('repository_url')
    if not repository_url:
        raise ValueError('Missing repository_url in OCI PURL')
    
    try:
        prefix = repository_url.split('/')[1]
    except IndexError:
        raise ValueError('Invalid repository_url in OCI PURL: insufficient path components')
    
    return f"{prefix}/{parsed_purl.name}" 