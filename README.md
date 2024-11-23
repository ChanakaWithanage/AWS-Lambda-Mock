
# Local AWS Lambda Environment Setup

This project demonstrates setting up a local development environment to test AWS Lambda functions using Docker.

## Setup Instructions

1. Clone this repository.
2. Navigate to the project directory:
   ```bash
   cd lambda-project
   ```
3. Build the Docker image:
   ```bash
   docker build -t local-lambda .
   ```
4. Run the container:
   ```bash
   docker run -p 9000:8080 local-lambda
   ```
5. Test the Lambda function locally:
   ```bash
   curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations"         -d '{"key": "value"}'
   ```

## Development Notes

- Modify `app/lambda_function.py` for your Lambda logic.
- Add Python dependencies to `requirements.txt`.
