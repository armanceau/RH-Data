import pandas as pd
import os

BRONZE_PATH = "../ds-bronze/"
SILVER_PATH = "../ds-silver/"

# On s'assure que les dossiers existent bien
os.makedirs(SILVER_PATH, exist_ok=True)

bronze_files = os.listdir(BRONZE_PATH)

for file in bronze_files:
    if file.endswith(".csv"): 
        print(f"Traitement du fichier : {file}")
        
        df = pd.read_csv(f"{BRONZE_PATH}/{file}")
        
        # On supprime les lignes avec des valeurs manquantes
        df_cleaned = df.dropna()

        if 'Age' in df_cleaned.columns:
            df_cleaned['Age'] = pd.to_numeric(df_cleaned['Age'], errors='coerce')

        # On sauvegarde dans ds-silver
        df_cleaned.to_csv(f"{SILVER_PATH}/{file}", index=False)
        print(f"Fichier nettoyé sauvegardé : {file}")
