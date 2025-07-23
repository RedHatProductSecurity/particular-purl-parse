#!/usr/bin/env python3
"""
Test runner for the particular_purl_parse module.
"""

import sys
import traceback

def run_tests():
    print("=" * 50)
    print("Testing particular_purl_parse module")
    print("=" * 50)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Import
    try:
        from particular_purl_parse import ps_component_from_purl
        print("✅ Test 1: Import successful")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 1: Import failed - {e}")
        tests_failed += 1
        return
    
    # Test 2: Basic PURL
    try:
        result = ps_component_from_purl("pkg:npm/lodash@4.17.21")
        assert result == "lodash"
        print(f"✅ Test 2: Basic PURL - {result}")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 2: Basic PURL failed - {e}")
        tests_failed += 1
    
    # Test 3: OCI PURL
    try:
        result = ps_component_from_purl("pkg:oci/nginx@1.21.0?repository_url=docker.io/library")
        assert result == "library/nginx"
        print(f"✅ Test 3: OCI PURL - {result}")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 3: OCI PURL failed - {e}")
        tests_failed += 1
    
    # Test 4: RPM PURL with rpmmod
    try:
        result = ps_component_from_purl("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx")
        assert result == "nginx/nginx"
        print(f"✅ Test 4: RPM PURL - {result}")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 4: RPM PURL failed - {e}")
        tests_failed += 1
    
    # Test 5: Error handling
    try:
        ps_component_from_purl("pkg:oci/nginx@1.21.0")  # Missing repository_url
        print("❌ Test 5: Should have raised error for missing repository_url")
        tests_failed += 1
    except ValueError as e:
        if "Missing repository_url" in str(e):
            print(f"✅ Test 5: Error handling - {e}")
            tests_passed += 1
        else:
            print(f"❌ Test 5: Unexpected error - {e}")
            tests_failed += 1
    
    # Test 6: Input validation
    try:
        ps_component_from_purl("")  # Empty string
        print("❌ Test 6: Should have raised error for empty string")
        tests_failed += 1
    except ValueError as e:
        if "PURL must be a non-empty string" in str(e):
            print(f"✅ Test 6: Input validation - {e}")
            tests_passed += 1
        else:
            print(f"❌ Test 6: Unexpected error - {e}")
            tests_failed += 1
    
    print("=" * 50)
    print(f"Results: {tests_passed} passed, {tests_failed} failed")
    
    if tests_failed == 0:
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed!")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1) 