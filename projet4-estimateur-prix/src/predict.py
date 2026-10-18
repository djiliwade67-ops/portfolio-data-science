import os
import pickle
import joblib
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "estimateur_prix_xgboost.pkl")
COLUMNS_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "X_columns.joblib")

TOP_TOWNS = [
    'Lekki', 'Ajah', 'Ikoyi', 'Ikeja', 'Ibeju Lekki',
    'Victoria Island (VI)', 'Port Harcourt', 'Ibadan', 'Gwarinpa', 'Magodo',
    'Life Camp', 'Guzape District', 'Katampe', 'Ikorodu',
    'Maitama District', 'Lokogoma District', 'Isheri North',
    'Owerri Municipal', 'Mowe Ofada', 'Isolo'
]

def predict_price(bedrooms, bathrooms, toilets, parking_space, town, state, title):
    """
    Reconstruit la ligne d'entrée avec exactitude par rapport aux colonnes de X
    et renvoie la prédiction du prix sous forme de nombre (float).
    """
    # 1. Charger le modèle et la liste des colonnes
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    model_columns = joblib.load(COLUMNS_PATH)

    # 2. Traitement de la ville
    town_clean_val = town if town in TOP_TOWNS else "Autre"

    # 3. Initialiser un DataFrame vide avec toutes les colonnes de X remplies de 0.0
    input_df = pd.DataFrame(0.0, index=[0], columns=model_columns)

    # 4. Assigner les variables numériques
    input_df.at[0, 'bedrooms'] = float(bedrooms)
    input_df.at[0, 'bathrooms'] = float(bathrooms)
    input_df.at[0, 'toilets'] = float(toilets)
    input_df.at[0, 'parking_space'] = float(parking_space)

    # 5. Activer les variables catégorielles (valeur 1.0 si la colonne existe dans X)
    col_town = f"town_clean_{town_clean_val}"
    col_state = f"state_{state}"
    col_title = f"title_{title}"

    if col_town in input_df.columns:
        input_df.at[0, col_town] = 1.0

    if col_state in input_df.columns:
        input_df.at[0, col_state] = 1.0

    if col_title in input_df.columns:
        input_df.at[0, col_title] = 1.0

    # 6. Prédiction
    prediction = model.predict(input_df)[0]
    return float(prediction)