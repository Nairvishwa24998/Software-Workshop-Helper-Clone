# SW2 Lab Helper

A Flask-based web application designed to help manage student assistance requests in a lab environment. Students can submit help requests with their seat numbers and topics, and Teaching Assistants (TAs) can view the queue in real-time.

## Features

- **Student Request Submission**: Students can submit help requests with their name, seat number, and topic
- **Real-time Queue Management**: Live queue updates using WebSocket technology
- **Seat Validation**: Automatic validation of seat numbers against lab layout
- **Topic Categorization**: Predefined topics for better request organization
- **Duplicate Prevention**: Prevents multiple requests from the same seat
- **Responsive Design**: Works on desktop and mobile devices

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sw2helperclone
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional)
   ```bash
   # Create a .env file in the root directory
   SECRET_KEY=your_secret_key_here
   ```

## Running the Application

1. **Start the Flask application**
   ```bash
   python run.py
   ```

2. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - The application will be available at the home page

## Usage

### For Students

1. **Submit a Help Request**
   - Go to the home page (`http://localhost:5000`)
   - Fill in your name
   - Select your seat number from the dropdown
   - Choose the topic you need help with
   - Click "Submit"

2. **View Queue Status**
   - Visit the queue page (`http://localhost:5000/queue`)
   - See your position in the queue
   - Monitor when TAs will reach you

### For Teaching Assistants

1. **Monitor the Queue**
   - Access the queue page (`http://localhost:5000/queue`)
   - View all pending student requests
   - See student names, seat numbers, topics, and request times

2. **Real-time Updates**
   - The queue updates automatically when new requests are submitted
   - No need to refresh the page

## Project Structure

```
sw2helperclone/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── views.py             # Route handlers and business logic
│   ├── dto.py               # Data Transfer Objects
│   ├── forms.py             # Flask-WTF form definitions
│   ├── check.py             # Additional utility functions
│   ├── static/              # Static files (CSS, JS, images)
│   ├── templates/           # HTML templates
│   └── data/                # Data storage directory
├── test/                    # Unit tests
│   ├── test_dto.py          # DTO tests
│   ├── test_simple.py       # Core functionality tests
│   ├── test_config_simple.py # Configuration tests
│   └── README.md            # Testing documentation
├── config.py                # Application configuration
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
├── pytest.ini              # Pytest configuration
├── run_tests.py            # Test runner script
└── README.md               # This file
```

## Testing

The project includes comprehensive unit tests to ensure reliability.

### Running Tests

```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=app --cov-report=term-missing

# Run specific test files
python -m pytest test/test_simple.py -v
python -m pytest test/test_config_simple.py -v

# Use the test runner script
python run_tests.py
```

### Test Coverage

The test suite covers:
- Student DTO creation and validation
- Queue management operations
- Seat number validation
- Configuration settings
- Edge cases and error handling

## Configuration

The application can be configured through the `config.py` file:

- **SECRET_KEY**: Flask secret key for session management
- **UPLOAD_FOLDER**: Directory for file uploads
- **MAX_CONTENT_LENGTH**: Maximum file upload size (1MB)

## Lab Seat Layout

The application supports the following seat layout:
- **Rows**: A, B, C, D, E, F, H, I, J, K, L, M, N, O, P (G is excluded)
- **Columns**: 1, 2, 3, 4, 5, 6, 7
- **Total Seats**: 105 seats (15 rows × 7 columns)

## Development

### Adding New Features

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write tests first** (TDD approach)
   ```bash
   # Add tests to appropriate test files
   python -m pytest test/test_simple.py -v
   ```

3. **Implement the feature**
   - Follow Flask best practices
   - Add proper error handling
   - Update documentation

4. **Run tests and ensure they pass**
   ```bash
   python -m pytest
   ```

### Code Style

- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change the port in run.py
   app.run(debug=True, port=5001)
   ```

2. **Import errors**
   - Ensure you're in the correct directory
   - Activate the virtual environment
   - Check that all dependencies are installed

3. **WebSocket connection issues**
   - Ensure the application is running
   - Check browser console for errors
   - Verify network connectivity

### Debug Mode

To run the application in debug mode:
```bash
export FLASK_ENV=development
python run.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page with request form |
| POST | `/` | Submit a new help request |
| GET | `/queue` | View the current queue |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- **Your Name** - Initial work

## Acknowledgments

- Flask framework and community
- Flask-SocketIO for real-time functionality
- Bootstrap for responsive design
- All contributors and testers

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the test documentation in `test/README.md`
3. Create an issue in the repository
4. Contact the development team 
