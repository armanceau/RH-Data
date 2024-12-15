import os
import pandas as pd
import numpy as np
from deltalake.writer import write_deltalake

SILVER_PATH = "../ds-silver/"
GOLD_PATH = "../ds-gold/"

os.makedirs(GOLD_PATH, exist_ok=True)

silver_files = os.listdir(SILVER_PATH)

for file in silver_files:
    if file.endswith(".csv"):  
        print(f"Traitement du fichier : {file}")
        
        df = pd.read_csv(f"{SILVER_PATH}/{file}")
        
        # 1. Catégorie age
        if 'Age' in df.columns:
            df['Age Group'] = pd.cut(
                df['Age'],
                bins=[0, 25, 35, 50, np.inf],
                labels=['Jeune', 'Adulte', 'Senior', 'Très Senior'],
                right=False
            )

        # 2. Indice de satisfaction
        if 'Job Satisfaction' in df.columns and 'Work-Life Balance' in df.columns:
            df['Combined Satisfaction'] = (
                df['Job Satisfaction'] * 0.6 + df['Work-Life Balance'] * 0.4
            )

        # 3. Niveau éducation 
        if 'Education Level' in df.columns:
            df['Education Category'] = df['Education Level'].map({
                'High School': 'Basique',
                'Bachelor': 'Intermédiaire',
                'Master': 'Avancé',
                'PhD': 'Très Avancé'
            }).fillna('Inconnu')

        # 4. Probabilités de changement carrière
        if 'Career Change' in df.columns:
            prob_career_change = df['Career Change'].mean()
            df['P(Career Change)'] = prob_career_change

        delta_path = f"{GOLD_PATH}/{file.replace('.csv', '')}"

        write_deltalake(delta_path, df)
        print(f"Fichier enrichi sauvegardé au format Delta : {delta_path}")