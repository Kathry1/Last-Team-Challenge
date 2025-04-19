1. Repository mit FastAPI-Projekt auf GitHub erstellen (erledigt ✅)

2. Projektstruktur:
   - main.py
   - model.pkl
   - requirements.txt
   - render.yaml (Konfigurationsdatei für Render)

3. Anforderungen (requirements.txt):
   fastapi
   uvicorn
   scikit-learn
   numpy
   pydantic

4. Neue Datei "render.yaml" hinzufügen mit folgendem Inhalt:

services:
  - type: web
    name: iris-api
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port 10000"
    plan: free

5. Deployment auf https://render.com:
   - Mit GitHub verbinden
   - Neues Web Service erstellen → „Deploy an existing GitHub repo“
   - Repository auswählen
   - Render liest automatisch die render.yaml und startet die App

6. Endpoints:
   - `/`     → API-Landingpage
   - `/predict`  → POST-Endpunkt für Vorhersagen mit JSON:
     {
       "features": [5.1, 3.5, 1.4, 0.2]
     }


