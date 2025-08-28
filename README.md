# Python FastAPI Hello World V1

A simple FastAPI Hello World application demonstrating basic project structure and setup.

## Project Structure

```
python-fastapi-hello-world/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── models/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/arch-faustocorrea/fastapi-hello-world-v1.git
cd fastapi-hello-world-v1
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Development Server

```bash
# Run with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or run directly
python -m app.main
```

The application will be available at:
- **API**: http://localhost:8000
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Hello World message
- `GET /health` - Health check endpoint

## Testing

Run the test suite:

```bash
pytest tests/
```

Run tests with coverage:

```bash
pytest tests/ --cov=app
```

## Dependencies

- **FastAPI** (≥0.104.1) - Modern, fast web framework for building APIs
- **Uvicorn** (≥0.24.0) - ASGI server implementation
- **Pydantic** (≥2.4.0) - Data validation using Python type annotations
- **python-multipart** (≥0.0.6) - For handling form data
- **pytest** (≥7.4.0) - Testing framework
- **httpx** (≥0.25.0) - HTTP client for testing

## Development Environment

The project is configured with:
- Basic logging configuration
- Health check endpoint
- Test infrastructure with pytest
- Proper .gitignore for Python projects
- FastAPI automatic interactive documentation

## Next Steps

1. Add more endpoints as needed
2. Implement data models in `app/models/`
3. Add database integration
4. Configure environment-specific settings
5. Add authentication and authorization
6. Implement proper error handling

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure everything works
4. Submit a pull request

## License

MIT License
