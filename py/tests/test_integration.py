"""
Integration tests for the particular_purl_parse package.
"""

import pytest
from particular_purl_parse import ps_component_from_purl


class TestPackageIntegration:
    """Integration tests for the package as a whole."""

    def test_package_import(self):
        """Test that the package can be imported correctly."""
        from particular_purl_parse import ps_component_from_purl
        assert callable(ps_component_from_purl)

    def test_package_version(self):
        """Test that the package version is accessible."""
        from particular_purl_parse import __version__
        assert isinstance(__version__, str)
        assert __version__ == "1.0.0"

    def test_package_all_exports(self):
        """Test that __all__ exports are correct."""
        from particular_purl_parse import __all__
        assert "ps_component_from_purl" in __all__

    def test_real_world_oci_examples(self):
        """Test with real-world OCI PURL examples."""
        examples = [
            ("pkg:oci/nginx@1.21.0?repository_url=docker.io/library", "library/nginx"),
            ("pkg:oci/redis@6.2.0?repository_url=quay.io/redis", "redis/redis"),
            ("pkg:oci/postgres@13.0?repository_url=registry.example.com/database", "database/postgres"),
        ]
        
        for purl, expected in examples:
            result = ps_component_from_purl(purl)
            assert result == expected, f"Failed for PURL: {purl}"

    def test_real_world_rpm_examples(self):
        """Test with real-world RPM PURL examples."""
        examples = [
            ("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx", "nginx/nginx"),
            ("pkg:rpm/fedora/python@3.9.0?rpmmod=python39", "python39/python"),
            ("pkg:rpm/centos/httpd@2.4.0?rpmmod=httpd", "httpd/httpd"),
        ]
        
        for purl, expected in examples:
            result = ps_component_from_purl(purl)
            assert result == expected, f"Failed for PURL: {purl}"

    def test_real_world_regular_examples(self):
        """Test with real-world regular PURL examples."""
        examples = [
            ("pkg:npm/lodash@4.17.21", "lodash"),
            ("pkg:pypi/requests@2.28.0", "requests"),
            ("pkg:maven/org.springframework/spring-core@5.3.0", "spring-core"),
            ("pkg:nuget/Newtonsoft.Json@13.0.1", "Newtonsoft.Json"),
            ("pkg:composer/monolog/monolog@2.0.0", "monolog"),
        ]
        
        for purl, expected in examples:
            result = ps_component_from_purl(purl)
            assert result == expected, f"Failed for PURL: {purl}"

    def test_mixed_qualifiers(self):
        """Test PURLs with multiple qualifiers."""
        # OCI with additional qualifiers
        purl = "pkg:oci/nginx@1.21.0?repository_url=docker.io/library&arch=amd64&os=linux&variant=alpine"
        result = ps_component_from_purl(purl)
        assert result == "library/nginx"
        
        # RPM with additional qualifiers
        purl = "pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx&arch=x86_64&distro=fedora&release=1"
        result = ps_component_from_purl(purl)
        assert result == "nginx/nginx"

    def test_edge_case_qualifiers(self):
        """Test edge cases with qualifiers."""
        # Empty qualifier values
        purl = "pkg:rpm/redhat/nginx@1.21.0?rpmmod=&arch=x86_64"
        result = ps_component_from_purl(purl)
        assert result == "nginx"  # Empty rpmmod should be ignored
        
        # Multiple rpmmod qualifiers (should use first one)
        purl = "pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx&rpmmod=nginx2"
        result = ps_component_from_purl(purl)
        assert result == "nginx/nginx"

    def test_complex_namespace_handling(self):
        """Test handling of complex namespace structures."""
        # Maven with complex namespace
        purl = "pkg:maven/org.springframework.boot/spring-boot-starter-web@2.7.0"
        result = ps_component_from_purl(purl)
        assert result == "spring-boot-starter-web"
        
        # NPM with scoped package
        purl = "pkg:npm/@angular/core@14.0.0"
        result = ps_component_from_purl(purl)
        assert result == "core"

    def test_version_handling(self):
        """Test that versions are handled correctly."""
        # Different version formats
        examples = [
            ("pkg:npm/lodash@4.17.21", "lodash"),
            ("pkg:npm/lodash@latest", "lodash"),
            ("pkg:npm/lodash@*", "lodash"),
            ("pkg:npm/lodash@^4.17.0", "lodash"),
        ]
        
        for purl, expected in examples:
            result = ps_component_from_purl(purl)
            assert result == expected, f"Failed for PURL: {purl}"

    def test_subpath_handling(self):
        """Test that subpaths are handled correctly."""
        # PURLs with subpaths
        purl = "pkg:npm/lodash@4.17.21#src/lodash.js"
        result = ps_component_from_purl(purl)
        assert result == "lodash"
        
        purl = "pkg:pypi/requests@2.28.0#requests/packages/urllib3"
        result = ps_component_from_purl(purl)
        assert result == "requests"

    def test_consistency_across_calls(self):
        """Test that the function returns consistent results."""
        purl = "pkg:oci/nginx@1.21.0?repository_url=docker.io/library"
        
        # Call multiple times
        results = [ps_component_from_purl(purl) for _ in range(10)]
        
        # All results should be the same
        assert len(set(results)) == 1
        assert results[0] == "library/nginx"

    def test_error_consistency(self):
        """Test that errors are consistent across calls."""
        purl = "pkg:oci/nginx@1.21.0"  # Missing repository_url
        
        # Should raise the same error multiple times
        for _ in range(5):
            with pytest.raises(ValueError, match="Missing repository_url in OCI PURL"):
                ps_component_from_purl(purl) 