"""
Tests for the core PURL parsing functionality.
"""

import pytest
from particular_purl_parse import ps_component_from_purl


class TestPsComponentFromPurl:
    """Test cases for the main ps_component_from_purl function."""

    def test_oci_purl_with_repository_url(self):
        """Test OCI PURL with valid repository_url qualifier."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=docker.io/library"
        result = ps_component_from_purl(purl)
        assert result == "library/nginx"

    def test_oci_purl_with_different_repository(self):
        """Test OCI PURL with different repository structure."""
        purl = "pkg:oci/redis@6.2.0?repository_url=quay.io/redis"
        result = ps_component_from_purl(purl)
        assert result == "redis/redis"

    def test_rpm_purl_with_rpmmod(self):
        """Test RPM PURL with rpmmod qualifier."""
        purl = "pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx"
        result = ps_component_from_purl(purl)
        assert result == "nginx/nginx"

    def test_rpm_purl_with_different_module(self):
        """Test RPM PURL with different rpmmod value."""
        purl = "pkg:rpm/fedora/python@3.9.0?rpmmod=python39"
        result = ps_component_from_purl(purl)
        assert result == "python39/python"

    def test_regular_npm_purl(self):
        """Test regular NPM PURL without special qualifiers."""
        purl = "pkg:npm/lodash@4.17.21"
        result = ps_component_from_purl(purl)
        assert result == "lodash"

    def test_regular_pypi_purl(self):
        """Test regular PyPI PURL without special qualifiers."""
        purl = "pkg:pypi/requests@2.28.0"
        result = ps_component_from_purl(purl)
        assert result == "requests"

    def test_regular_maven_purl(self):
        """Test regular Maven PURL without special qualifiers."""
        purl = "pkg:maven/org.springframework/spring-core@5.3.0"
        result = ps_component_from_purl(purl)
        assert result == "spring-core"

    def test_oci_purl_without_repository_url(self):
        """Test OCI PURL without repository_url qualifier should raise error."""
        purl = "pkg:oci/nginx@1.21.0"
        with pytest.raises(ValueError, match="Missing repository_url in OCI PURL"):
            ps_component_from_purl(purl)

    def test_oci_purl_with_empty_repository_url(self):
        """Test OCI PURL with empty repository_url qualifier."""
        purl = "pkg:oci/nginx@1.21.0?repository_url="
        with pytest.raises(ValueError, match="Missing repository_url in OCI PURL"):
            ps_component_from_purl(purl)

    def test_oci_purl_with_invalid_repository_url(self):
        """Test OCI PURL with invalid repository_url structure."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=invalid"
        with pytest.raises(
            ValueError,
            match="Invalid repository_url in OCI PURL: insufficient path components",
        ):
            ps_component_from_purl(purl)

    def test_oci_purl_with_single_slash_repository_url(self):
        """Test OCI PURL with repository_url that has only one slash."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=docker.io"
        with pytest.raises(
            ValueError,
            match="Invalid repository_url in OCI PURL: insufficient path components",
        ):
            ps_component_from_purl(purl)

    def test_rpm_purl_without_rpmmod(self):
        """Test RPM PURL without rpmmod qualifier should return just name."""
        purl = "pkg:rpm/redhat/nginx@1.21.0"
        result = ps_component_from_purl(purl)
        assert result == "nginx"

    def test_complex_oci_repository_url(self):
        """Test OCI PURL with complex repository URL structure."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=registry.example.com/team/project"
        result = ps_component_from_purl(purl)
        assert result == "team/nginx"

    def test_oci_purl_with_version_and_other_qualifiers(self):
        """Test OCI PURL with version and other qualifiers."""
        purl = (
            "pkg:oci/nginx@1.21.0?repository_url=docker.io/library&arch=amd64&os=linux"
        )
        result = ps_component_from_purl(purl)
        assert result == "library/nginx"

    def test_rpm_purl_with_version_and_other_qualifiers(self):
        """Test RPM PURL with version and other qualifiers."""
        purl = "pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx&arch=x86_64&distro=fedora"
        result = ps_component_from_purl(purl)
        assert result == "nginx/nginx"


class TestPsComponentOci:
    """Test cases for the _ps_component_oci helper function."""

    def test_valid_repository_url(self):
        """Test with valid repository URL."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=docker.io/library"
        result = ps_component_from_purl(purl)
        assert result == "library/nginx"

    def test_missing_repository_url(self):
        """Test with missing repository_url qualifier."""
        purl = "pkg:oci/nginx@1.21.0"
        with pytest.raises(ValueError, match="Missing repository_url in OCI PURL"):
            ps_component_from_purl(purl)

    def test_empty_repository_url(self):
        """Test with empty repository_url qualifier."""
        purl = "pkg:oci/nginx@1.21.0?repository_url="
        with pytest.raises(ValueError, match="Missing repository_url in OCI PURL"):
            ps_component_from_purl(purl)

    def test_invalid_repository_url_structure(self):
        """Test with invalid repository URL structure."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=invalid"
        with pytest.raises(
            ValueError,
            match="Invalid repository_url in OCI PURL: insufficient path components",
        ):
            ps_component_from_purl(purl)

    def test_single_slash_repository_url(self):
        """Test with repository URL that has only one slash."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=docker.io"
        with pytest.raises(
            ValueError,
            match="Invalid repository_url in OCI PURL: insufficient path components",
        ):
            ps_component_from_purl(purl)

    def test_complex_repository_url(self):
        """Test with complex repository URL structure."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=registry.example.com/team/project"
        result = ps_component_from_purl(purl)
        assert result == "team/nginx"


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_purl_string(self):
        """Test with empty PURL string."""
        with pytest.raises(ValueError, match="PURL must be a non-empty string"):
            ps_component_from_purl("")

    def test_invalid_purl_format(self):
        """Test with invalid PURL format."""
        with pytest.raises(ValueError, match="Invalid PURL format"):
            ps_component_from_purl("invalid-purl")

    def test_missing_pkg_scheme(self):
        """Test with missing pkg scheme."""
        with pytest.raises(ValueError, match="Invalid PURL format"):
            ps_component_from_purl("oci/nginx@1.21.0")

    def test_none_input(self):
        """Test with None input."""
        with pytest.raises(ValueError, match="PURL must be a non-empty string"):
            ps_component_from_purl(None)

    def test_non_string_input(self):
        """Test with non-string input."""
        with pytest.raises(ValueError, match="PURL must be a non-empty string"):
            ps_component_from_purl(123)

    def test_very_long_purl(self):
        """Test with very long PURL string."""
        long_purl = "pkg:oci/" + "a" * 1000 + "@1.0.0?repository_url=docker.io/library"
        result = ps_component_from_purl(long_purl)
        assert result == f"library/{'a' * 1000}"

    def test_special_characters_in_name(self):
        """Test with special characters in package name."""
        purl = "pkg:oci/my-package@1.0.0?repository_url=docker.io/library"
        result = ps_component_from_purl(purl)
        assert result == "library/my-package"

    def test_unicode_characters(self):
        """Test with Unicode characters in package name."""
        purl = "pkg:oci/测试包@1.0.0?repository_url=docker.io/library"
        result = ps_component_from_purl(purl)
        assert result == "library/测试包"
