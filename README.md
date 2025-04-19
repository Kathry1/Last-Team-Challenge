# 🌟 Last Team Challenge - ML Deployment

[![Render Status](https://img.shields.io/badge/Deployed%20on-Render-764ABC?style=for-the-badge&logo=render&logoColor=white)](https://last-team-challenge.onrender.com)

## 🔖 Project Description
Deployment of a FastAPI application with a machine learning model for Iris classification.
The trained model is exposed via a REST API and publicly available on [Render.com](https://render.com).

---

## 📁 Project Structure

```
Last-Team-Challenge/
├── main.py              # FastAPI application
├── train_model.py       # Training script to generate train_model.pkl
├── train_model.pkl      # Pickled ML model
├── requirements.txt     # Python dependencies
├── render.yaml          # Render configuration for automated deployment
├── README.md            # Project description
└── Notebook_LastTeamChallenge.ipynb  # Original analysis notebook
```

---

## 🚀 Deployment Guide (Render)

### 1. Requirements
- GitHub repository available
- Render account: https://render.com (Free plan is sufficient)

### 2. Deploy in 3 Steps

1. Connect GitHub to Render and create a "New Web Service"
2. Select your repository → Render automatically detects `render.yaml`
3. Start Command from `render.yaml`:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```

**The app is live within minutes!**

---

## 🚪 Live Endpoints

**Base URL:** [`https://last-team-challenge.onrender.com`](https://last-team-challenge.onrender.com)

| Endpoint     | Method | Description                                          |
|--------------|--------|------------------------------------------------------|
| `/`          | GET    | Welcome page and API instructions                   |
| `/predict`   | POST   | Accepts JSON with `features`, returns prediction    |
| `/status`    | GET    | Returns model status, type, and version             |

### Example request to `/predict`
```json
POST /predict
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

Response:
```json
{
  "prediction": 0
}
```

---

## 🌐 Tools & Libraries

- **FastAPI** - Web framework for APIs
- **scikit-learn** - Model training
- **Uvicorn** - ASGI server for deployment
- **Render** - Cloud deployment platform

---

## 🚀 Project Status
- [x] ML model trained & stored
- [x] API developed and documented
- [x] Deployed live on Render
- [x] Endpoints tested successfully

---

## 👤 Author
**Kathrin Fuchs**  
Project developed during the Data Science & Machine Learning Bootcamp at The Bridge


