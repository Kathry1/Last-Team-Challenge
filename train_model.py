from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import pickle

# Modell trainieren
X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Modell speichern
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
