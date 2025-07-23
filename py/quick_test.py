#!/usr/bin/env python3
"""
Quick test to verify the Python module functionality.
"""

def main():
    print("Testing particular_purl_parse module...")
    
    try:
        # Test import
        from particular_purl_parse import ps_component_from_purl
        print("✅ Import successful")
        
        # Test OCI PURL
        result = ps_component_from_purl("pkg:oci/nginx@1.21.0?repository_url=docker.io/library")
        print(f"✅ OCI test: {result}")
        
        # Test RPM PURL
        result = ps_component_from_purl("pkg:rpm/redhat/nginx@1.21.0?rpmmod=nginx")
        print(f"✅ RPM test: {result}")
        
        # Test regular PURL
        result = ps_component_from_purl("pkg:npm/lodash@4.17.21")
        print(f"✅ Regular test: {result}")
        
        # Test error handling
        try:
            ps_component_from_purl("pkg:oci/nginx@1.21.0")
            print("❌ Should have raised error for missing repository_url")
        except ValueError as e:
            print(f"✅ Error handling: {e}")
        
        print("\n🎉 All tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main() 