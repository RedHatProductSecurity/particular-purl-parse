from particular_purl_parse import ps_component_from_purl


class TestParticularPurlParse:
    def test_regular_purl(self):
        result = ps_component_from_purl("pkg:npm/lodash@4.17.21")

        assert result == "lodash"

    def test_rpm_purl(self):
        result = ps_component_from_purl("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx")

        assert result == "nginx/nginx"

    def test_oci_purl(self):
        result = ps_component_from_purl(
            "pkg:oci/nginx@1.21.0?repository_url=docker.io/library"
        )

        assert result == "library/nginx"

    def test_oci_purl_missing_repo(self):
        try:
            ps_component_from_purl("pkg:oci/nginx@1.21.0")
        except ValueError as e:
            assert str(e) == "Missing repository_url in OCI PURL"
        else:
            assert False, "Expected ValueError for missing repository_url"

    def test_oci_purl_invalid_repo(self):
        try:
            ps_component_from_purl("pkg:oci/nginx@1.21.0?repository_url=docker.io")
        except ValueError as e:
            assert (
                str(e)
                == "Invalid repository_url in OCI PURL: insufficient path components"
            )
        else:
            assert False, "Expected ValueError for invalid repository_url"
