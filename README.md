# Payment Platform

A minimal FastAPI-based payment platform that supports creating, authorizing, capturing, and refunding payments backed by SQLite storage. It now ships with a colorful, glassy homepage, Google-ready sign-up page, and a real-time currency converter.

## Features
- Create payments with amount, currency, and optional description
- Retrieve individual payments or list recent payments
- Authorize and capture funds with simple state validation
- Refund captured payments
- Persist data in SQLite via SQLModel
- Glassmorphic homepage and sign-up experience with Google Identity button
- Real-time currency converter powered by exchangerate.host

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

4. Explore the glassy homepage at `http://127.0.0.1:8000/` and the dedicated sign-up screen at `http://127.0.0.1:8000/signup`.

### Frontend notes
- The Google sign-up button uses Google Identity Services; replace `YOUR_GOOGLE_CLIENT_ID` in `app/static/index.html` and `app/static/signup.html` with your OAuth client ID and set `data-login_uri` if you want to handle tokens server-side.
- The currency converter fetches live rates from exchangerate.host; ensure outbound HTTPS is permitted in your environment for live conversions.

## Running Tests
Execute the test suite with pytest:
```bash
pytest
```
