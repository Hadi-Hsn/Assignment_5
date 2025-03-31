# Sentiment Analysis API

This project provides a RESTful API for sentiment analysis using the Azure OpenAI `gpt-35-turbo-16k` model. The API accepts user input text and returns the sentiment analysis result.

## Features
- Uses Azure OpenAI `chat/completions` endpoint.
- Implements FastAPI for the API framework.
- Securely manages API keys and endpoint URLs using environment variables.

## Prerequisites
1. Python 3.8 or higher.
2. Azure OpenAI resource with a deployed model (e.g., `gpt-35-turbo-16k`).
3. Required Python libraries (see `requirements.txt`).

## Setup Instructions
1. Clone the repository and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add the following:
   ```plaintext
   OPENAI_API_KEY=your_azure_openai_api_key_here
   OPENAI_API_URL=https://<your-resource-name>.cognitiveservices.azure.com/openai/deployments/<deployment-name>/chat/completions?api-version=2025-01-01-preview
   ```
   Replace `<your-resource-name>` and `<deployment-name>` with your Azure OpenAI resource details.

4. Start the FastAPI server:
   ```bash
   python main.py
   ```

## API Usage
### Endpoint
`POST /analyze-sentiment/`

### Request Body
```json
{
  "text": "I like this product! It is amazing."
}
```

### Response
```json
{
  "sentiment": "Positive."
}
```

## Testing with `curl`
Run the following command to test the API:
```bash
curl -X POST "http://127.0.0.1:8000/analyze-sentiment/" -H "Content-Type: application/json" -d '{"text": "I like this product! It is amazing."}'
```

## License
This project is licensed under the MIT License.