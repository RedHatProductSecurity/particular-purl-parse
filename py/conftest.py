"""
Pytest configuration and common fixtures.
"""

import pytest


@pytest.fixture
def sample_oci_purls():
    """Sample OCI PURLs for testing."""
    return [
        "pkg:oci/nginx@1.21.0?repository_url=docker.io/library",
        "pkg:oci/redis@6.2.0?repository_url=quay.io/redis",
        "pkg:oci/postgres@13.0?repository_url=registry.example.com/database",
    ]


@pytest.fixture
def sample_rpm_purls():
    """Sample RPM PURLs for testing."""
    return [
        "pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx",
        "pkg:rpm/fedora/python@3.9.0?rpmmod=python39",
        "pkg:rpm/centos/httpd@2.4.0?rpmmod=httpd",
    ]


@pytest.fixture
def sample_regular_purls():
    """Sample regular PURLs for testing."""
    return [
        "pkg:npm/lodash@4.17.21",
        "pkg:pypi/requests@2.28.0",
        "pkg:maven/org.springframework/spring-core@5.3.0",
    ]


@pytest.fixture
def invalid_purls():
    """Invalid PURLs for testing error handling."""
    return [
        "",  # Empty string
        "invalid-purl",  # No pkg scheme
        "oci/nginx@1.21.0",  # Missing pkg scheme
        "pkg:oci/nginx@1.21.0",  # Missing repository_url
        "pkg:oci/nginx@1.21.0?repository_url=invalid",  # Invalid repository_url
    ]


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )


def pytest_collection_modifyitems(config, items):
    """Automatically mark test classes and functions."""
    for item in items:
        # Mark integration tests
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        # Mark unit tests
        elif "test_core" in item.nodeid:
            item.add_marker(pytest.mark.unit) 