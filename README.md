# Taxi Fare Prediction using MLOps

## Tech Stack

- Python
- Scikit-Learn
- XGBoost
- DVC
- Feast
- MLflow
- FastAPI
- Docker
- GitHub Actions

---

## Project Pipeline

CSV Dataset

↓

Data Validation

↓

Data Preprocessing

↓

Feature Engineering

↓

Feature Store

↓

Model Training

↓

Evaluation

↓

MLflow

↓

FastAPI

↓

Docker

↓

Deployment

---

## Install

```bash
pip install -r requirements.txt
```

---

## Train

```bash
python src/pipelines/training_pipeline.py
```

---

## Run API

```bash
uvicorn api.app:app --reload
```