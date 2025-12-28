#!/usr/bin/env python3
"""
Test suite for gorkTerms.py - Machine Learning Terminology Dictionary

This test verifies that:
1. The module can be imported successfully
2. All variables are properly defined as strings
3. All variables contain meaningful descriptions (not empty strings)
4. Variable names follow camelCase convention where appropriate
"""

import sys
import os
import re

# Add the parent directory to the path so we can import gorkTerms
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

def test_import():
    """Test that gorkTerms module can be imported successfully"""
    try:
        import gorkTerms
        return True, gorkTerms
    except ImportError as e:
        return False, f"Failed to import gorkTerms: {e}"

def test_all_variables_are_strings(module):
    """Test that all variables in the module are strings"""
    errors = []
    for name in dir(module):
        if not name.startswith('_'):  # Skip private/special attributes
            value = getattr(module, name)
            if not isinstance(value, str):
                errors.append(f"{name} is not a string (type: {type(value).__name__})")
    return len(errors) == 0, errors

def test_no_empty_descriptions(module):
    """Test that no variables contain empty string descriptions"""
    errors = []
    for name in dir(module):
        if not name.startswith('_'):
            value = getattr(module, name)
            if isinstance(value, str) and len(value.strip()) == 0:
                errors.append(f"{name} has empty description")
    return len(errors) == 0, errors

def test_meaningful_descriptions(module):
    """Test that descriptions are sufficiently detailed (at least 10 words)"""
    errors = []
    for name in dir(module):
        if not name.startswith('_'):
            value = getattr(module, name)
            if isinstance(value, str):
                word_count = len(value.split())
                if word_count < 10:
                    errors.append(f"{name} description too short ({word_count} words): '{value}'")
    return len(errors) == 0, errors

def test_camelcase_variables(module):
    """Test that multi-word variables follow camelCase convention"""
    errors = []
    camelcase_pattern = re.compile(r'^[a-z]+([A-Z][a-z]*)*$')

    for name in dir(module):
        if not name.startswith('_') and not name.islower():
            # Check if it follows camelCase pattern
            if not camelcase_pattern.match(name):
                errors.append(f"{name} does not follow camelCase convention")

    return len(errors) == 0, errors

def run_all_tests():
    """Run all tests and report results"""
    print("Running tests for gorkTerms.py...")
    print("=" * 50)

    # Test import
    success, result = test_import()
    if not success:
        print(f"❌ IMPORT TEST FAILED: {result}")
        return False
    else:
        module = result
        print("✅ Import test passed")

    # Test string types
    success, errors = test_all_variables_are_strings(module)
    if not success:
        print("❌ STRING TYPE TEST FAILED:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("✅ All variables are strings")

    # Test no empty descriptions
    success, errors = test_no_empty_descriptions(module)
    if not success:
        print("❌ EMPTY DESCRIPTION TEST FAILED:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("✅ No empty descriptions found")

    # Test meaningful descriptions
    success, errors = test_meaningful_descriptions(module)
    if not success:
        print("❌ MEANINGFUL DESCRIPTION TEST FAILED:")
        for error in errors[:5]:  # Show first 5 errors to avoid spam
            print(f"  - {error}")
        if len(errors) > 5:
            print(f"  ... and {len(errors) - 5} more")
        return False
    else:
        print("✅ All descriptions are sufficiently detailed")

    # Test camelCase convention
    success, errors = test_camelcase_variables(module)
    if not success:
        print("❌ CAMELCASE TEST FAILED:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
        return False
    else:
        print("✅ CamelCase convention followed")

    print("=" * 50)
    print("🎉 ALL TESTS PASSED!")
    return True

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
