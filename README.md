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

## Project Generation Prompt

```
Customer Churn Prediction Web Application

Goal:
Build a full-stack web application to predict which insurance policyholders are likely to cancel their policies. The app should use customer engagement metrics, claim patterns, and payment history to assess churn risk. Results will help design retention strategies and offer targeted incentives to high-risk customers.

Features:
- Backend API (FastAPI):
  - CRUD operations for customer records
  - Churn prediction endpoint using a trained ML model
  - Business logic for risk scoring
  - Data validation and error handling
- Machine Learning Model:
  - Train a model using customer engagement, claims, and payment history
  - Save and load model for inference
  - Update churn risk scores for all customers
- Frontend (React):
  - UI for entering customer data and viewing predictions
  - Customer management (view, add, edit, delete)
  - Display churn risk scores and insights
  - Visualization (charts, tables)
- Data:
  - Scripts to populate and manage sample data
- Testing:
  - Unit and integration tests for backend and frontend
- Documentation:
  - Clear setup, usage, and API instructions
  - Project prompt and requirements

Tech Stack:
- Python (FastAPI, scikit-learn, pandas, SQLAlchemy)
- React (UI, Axios, Chart.js)
- SQLite (local database)

Outcome:
A maintainable, extensible web application for insurance customer churn prediction, with a clean codebase and clear documentation.
```
