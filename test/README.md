# Testing Guide for SW2 Lab Helper

This directory contains simple, effective unit tests for the SW2 Lab Helper Flask application.

## Test Structure

```
test/
├── test_dto.py             # Data Transfer Object tests (original)
├── test_simple.py          # Simple unit tests for core functionality
├── test_config_simple.py   # Configuration tests
└── README.md               # This file
```

## Test Categories

### Unit Tests
- **test_dto.py**: Tests for the Student data transfer object (original)
- **test_simple.py**: Tests for core functionality (Student, queue management, seat validation)
- **test_config_simple.py**: Tests for application configuration

## Running Tests

### Prerequisites
Install the required testing dependencies:
```bash
pip install -r requirements.txt
```

### Basic Test Commands

1. **Run all tests:**
   ```bash
   python -m pytest
   ```

2. **Run tests with coverage:**
   ```bash
   python -m pytest --cov=app --cov-report=term-missing
   ```

3. **Run specific test categories:**
   ```bash
   # Unit tests only
   python -m pytest -m unit
   
   # Integration tests only
   python -m pytest -m integration
   ```

4. **Run specific test file:**
   ```bash
   python -m pytest test/test_dto.py
   ```

5. **Run tests in verbose mode:**
   ```bash
   python -m pytest -v
   ```

### Using the Test Runner Script

The `run_tests.py` script provides a convenient way to run tests:

```bash
# Run all tests with coverage
python run_tests.py

# Run only unit tests
python run_tests.py --type unit

# Run only integration tests
python run_tests.py --type integration

# Run tests without coverage
python run_tests.py --no-coverage

# Run tests in quiet mode
python run_tests.py --quiet

# Run a specific test file
python run_tests.py --file test/test_dto.py
```

## Test Coverage

The test suite provides comprehensive coverage of:

- **Student DTO**: Object creation, validation, and string representation
- **Form Validation**: All form fields, validation rules, and error handling
- **Route Handling**: GET/POST requests, form submission, error responses
- **Queue Management**: Adding students, duplicate detection, seat validation
- **WebSocket Communication**: Connection, disconnection, and event handling
- **Configuration**: Environment variables, default values, path handling
- **Integration Flows**: Complete user journeys from form submission to queue updates

## Test Fixtures

The `conftest.py` file provides several useful fixtures:

- `client`: Flask test client with proper configuration
- `socketio_client`: SocketIO test client
- `sample_student_data`: Sample data for testing
- `sample_student`: Sample Student object

## Writing New Tests

### Adding Unit Tests
1. Create a new test file following the naming convention `test_*.py`
2. Use the `@pytest.mark.unit` decorator for unit tests
3. Follow the existing test structure with descriptive class and method names

Example:
```python
import pytest
from app.your_module import YourClass

class TestYourClass:
    @pytest.mark.unit
    def test_your_method(self):
        # Your test code here
        pass
```

### Adding Integration Tests
1. Use the `@pytest.mark.integration` decorator
2. Test complete workflows rather than individual functions
3. Use the provided fixtures for consistent test setup

Example:
```python
import pytest

class TestYourIntegration:
    @pytest.mark.integration
    def test_complete_workflow(self, client):
        # Test complete user workflow
        pass
```

## Test Best Practices

1. **Descriptive Names**: Use clear, descriptive test method names
2. **Arrange-Act-Assert**: Structure tests with clear sections
3. **Isolation**: Each test should be independent and not rely on other tests
4. **Cleanup**: Use fixtures to set up and tear down test data
5. **Edge Cases**: Test both valid and invalid inputs
6. **Error Conditions**: Test error handling and edge cases

## Coverage Reports

After running tests with coverage, you'll get:
- **Terminal output**: Shows missing lines
- **HTML report**: Detailed coverage report in `htmlcov/` directory
- **XML report**: Coverage data for CI/CD integration

## Continuous Integration

The test suite is designed to work with CI/CD systems:
- All tests are independent and can run in parallel
- Coverage reports are generated in multiple formats
- Exit codes properly indicate test success/failure

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you're running tests from the project root
2. **Missing Dependencies**: Install all requirements with `pip install -r requirements.txt`
3. **Database Issues**: Tests use in-memory data structures, no database setup required
4. **WebSocket Issues**: SocketIO tests may need proper event loop setup

### Debugging Tests

To debug failing tests:
```bash
# Run with more verbose output
python -m pytest -vvv

# Run a specific failing test
python -m pytest test/test_file.py::TestClass::test_method -v

# Run with print statement output
python -m pytest -s
```

## Contributing

When adding new features:
1. Write tests first (TDD approach)
2. Ensure all tests pass
3. Maintain or improve test coverage
4. Update this README if adding new test categories 