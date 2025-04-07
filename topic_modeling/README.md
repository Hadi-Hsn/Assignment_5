# Topic Modeling Service

A Flask-based REST API service that uses OpenAI's GPT models to extract the main topic from given text input.

## Features

- REST API endpoint for topic extraction
- Uses OpenAI's GPT models for text analysis
- Structured output using Pydantic models
- Health check endpoint for service monitoring

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the server:
```bash
python app.py
```

2. The service will be available at `http://localhost:5000`

### API Endpoints

#### Health Check
- **GET** `/health`
- Returns service status

#### Topic Extraction
- **POST** `/predict/topic`
- Request body:
```json
{
    "text": "Your text here"
}
```
- Response:
```json
{
    "Text topic": "extracted_topic"
}
```

## Project Structure

- `app.py`: Flask application and API endpoints
- `service.py`: Core business logic for topic extraction
- `model.py`: Pydantic models for structured output
- `requirements.txt`: Project dependencies

## Dependencies

- Flask: Web framework
- llama-index: LLM integration
- pydantic: Data validation

## Error Handling

The service includes error handling for:
- Missing text input
- Invalid requests
- Server errors
