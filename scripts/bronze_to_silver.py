import os
import pandas as pd
from deltalake.writer import write_deltalake

BRONZE_PATH = "../ds-bronze/"
SILVER_PATH = "../ds-silver/"

os.makedirs(SILVER_PATH, exist_ok=True)

bronze_files = os.listdir(BRONZE_PATH)

for file in bronze_files:
    if file.endswith(".csv"):
        print(f"Traitement du fichier : {file}")
        
        df = pd.read_csv(f"{BRONZE_PATH}/{file}")
        
        df_cleaned = df.dropna()
        
        if 'Age' in df_cleaned.columns:
            df_cleaned['Age'] = pd.to_numeric(df_cleaned['Age'], errors='coerce')  # Convertir Age en numérique
        
        # Conversion en format Delta
        delta_path = f"{SILVER_PATH}/{file.replace('.csv', '')}"
        write_deltalake(delta_path, df_cleaned)
        print(f"Fichier nettoyé sauvegardé en format Delta : {delta_path}")
