# Last-Team-Challenge


## 📌 Projektbeschreibung
Deployment einer FastAPI-Anwendung mit Machine Learning Modell für Iris-Klassifikation.

## 🚀 Deployment auf Render

### Struktur
- `main.py`
- `model.pkl`
- `requirements.txt`
- `render.yaml`

### Anforderungen (requirements.txt):
   fastapi
   uvicorn
   scikit-learn
   numpy
   pydantic


### Deploy-Anleitung
1. Mit GitHub verbinden
2. Web Service auf https://render.com erstellen
3. Render erkennt automatisch `render.yaml`
4. Endpoints:
   - `/`
   - `/predict` → POST mit JSON: {"features": [5.1, 3.5, 1.4, 0.2]}
