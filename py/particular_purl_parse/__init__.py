"""
Particular PURL Parse - A library for parsing PackageURL (PURL) strings.

This module provides functionality to extract component information from PURL strings,
with special handling for OCI and RPM package types.
"""

from .core import ps_component_from_purl

__version__ = "1.0.0"
__all__ = ["ps_component_from_purl"] 