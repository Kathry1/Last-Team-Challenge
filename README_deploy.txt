1. Bei https://www.pythonanywhere.com registrieren und einloggen.

2. Eine neue "Web App" erstellen:
   - Framework: "Manual configuration"
   - Python-Version: z. B. Python 3.10

3. Dateien hochladen (via "Files"):
   - `main.py`
   - `model.pkl`
   - `requirements.txt`

4. Im Bash-Terminal:
   > pip install --user -r requirements.txt

5. WSGI-Konfiguration anpassen:
   Öffne unter "Web" → "WSGI configuration file" und ändere:
   ```python
   import sys
   path = '/home/yourusername/ml_api'  # Pfad anpassen
   if path not in sys.path:
       sys.path.append(path)

   from main import app as application
