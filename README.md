# Payment Platform

A minimal FastAPI-based payment platform that supports creating, authorizing, capturing, and refunding payments backed by SQLite storage.

## Features
- Create payments with amount, currency, and optional description
- Retrieve individual payments or list recent payments
- Authorize and capture funds with simple state validation
- Refund captured payments
- Persist data in SQLite via SQLModel

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Interact with the API using the automatically generated docs at `http://127.0.0.1:8000/docs`.

## Running Tests
Execute the test suite with pytest:
```bash
pytest
```
