# Customer Churn Prediction Web Application

This project predicts which insurance policyholders are likely to cancel their policies, helping design retention strategies and targeted incentives.

## Structure
- **backend/**: FastAPI app, ML model, database, business logic, API endpoints, and tests
- **frontend/**: React app for UI, customer management, prediction form, and visualization
- **data/**: Scripts for populating and managing sample data

## Setup
1. Install backend dependencies:
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
2. Install frontend dependencies:
   ```sh
   cd frontend
   npm install
   ```
3. (Optional) Populate the database with sample data:
   ```sh
   cd backend
   ../.venv/bin/python -m app.scripts.populate_db
   ```
4. Train the churn prediction model:
   ```sh
   cd backend
   ../.venv/bin/python -m app.ml.train_model
   ```
5. Start the backend server:
   ```sh
   cd backend
   ../.venv/bin/uvicorn app.main:app --reload
   ```
6. Start the frontend server:
   ```sh
   cd frontend
   npm start
   ```

## Features
- Predict customer churn risk using engagement, claims, and payment history
- Manage customer records via UI and API
- View churn risk scores and insights
- Expandable for more features and model improvements

## Testing
- Backend: Run unit and integration tests with pytest
  ```sh
  cd backend
  ../.venv/bin/python -m pytest tests/
  ```
- Frontend: Add and run tests in `frontend/tests/`

## Documentation
- API documentation available at `/docs` when backend is running
- Update this README as features evolve
