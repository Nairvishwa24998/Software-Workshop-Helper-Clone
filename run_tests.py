#!/usr/bin/env python3
"""
Simple test runner script for the SW2 Lab Helper application.
"""

import sys
import subprocess


def run_tests():
    """Run all tests."""
    cmd = ['python', '-m', 'pytest', '-v', '--cov=app', '--cov-report=term-missing']
    
    print(f"Running tests: {' '.join(cmd)}")
    print("=" * 50)
    
    try:
        result = subprocess.run(cmd, check=True)
        print("\n" + "=" * 50)
        print("✅ All tests passed!")
        return True
    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 50)
        print(f"❌ Tests failed with exit code {e.returncode}")
        return False


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1) 