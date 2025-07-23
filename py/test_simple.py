#!/usr/bin/env python3
"""
Simple test script to verify the Python module functionality.
"""

def test_import():
    """Test that the module can be imported."""
    try:
        from particular_purl_parse import ps_component_from_purl
        print("✅ Import successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality."""
    try:
        from particular_purl_parse import ps_component_from_purl
        
        # Test OCI PURL
        result = ps_component_from_purl("pkg:oci/nginx@1.21.0?repository_url=docker.io/library")
        assert result == "library/nginx"
        print("✅ OCI PURL test passed")
        
        # Test RPM PURL with rpmmod
        result = ps_component_from_purl("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx")
        assert result == "nginx/nginx"
        print("✅ RPM PURL test passed")
        
        # Test regular PURL
        result = ps_component_from_purl("pkg:npm/lodash@4.17.21")
        assert result == "lodash"
        print("✅ Regular PURL test passed")
        
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def test_error_handling():
    """Test error handling."""
    try:
        from particular_purl_parse import ps_component_from_purl
        
        # Test OCI PURL without repository_url
        try:
            ps_component_from_purl("pkg:oci/nginx@1.21.0")
            print("❌ Should have raised ValueError for missing repository_url")
            return False
        except ValueError as e:
            if "Missing repository_url" in str(e):
                print("✅ Error handling test passed")
                return True
            else:
                print(f"❌ Unexpected error message: {e}")
                return False
                
    except Exception as e:
        print(f"❌ Error handling test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Running simple tests for particular_purl_parse module...")
    print()
    
    tests = [
        test_import,
        test_basic_functionality,
        test_error_handling,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    exit(main()) 