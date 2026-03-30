# ML Model API with FastAPI & Docker

## Overview
This project demonstrates how to deploy a machine learning model using FastAPI and Docker. The API provides an endpoint to send input data and receive predictions.

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Docker

## Project Structure
ml-api-project/
- app.py
- model.pkl
- requirements.txt
- Dockerfile
- .gitignore
- README.md

## Run Locally

### Without Docker
1. Install dependencies:
pip install -r requirements.txt

2. Run the server:
uvicorn app:app --reload

3. Open in browser:
http://localhost:8000/docs

### With Docker
1. Build image:
docker build -t ml-api .

2. Run container:
docker run -p 8000:8000 ml-api

3. Open:
http://localhost:8000/docs

## API Endpoints

### GET /
Returns API status

Response:
{
  "message": "API is working"
}

### POST /predict

Request:
{
  "input": 5
}

Response:
{
  "prediction": 10
}

## Example (cURL)
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"input\": 5}"

## Features
- FastAPI REST API
- Model inference endpoint
- Docker containerization
- Interactive API documentation

  ## 📄 Report
[Download Report](ML_API_Report.pdf)

## Author
Archana
