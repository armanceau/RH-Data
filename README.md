# RH-Data
Projet de big data


## Objectifs : 

_TODO_

## Structure du projet

Le projet est organisé en trois scripts principaux :

- `bronze_to_silver.py` : Transforme les données de l'étape **Bronze** vers l'étape **Silver**. Ce script nettoie les données et les enregistre en format Delta.
- `silver_to_gold.py` : Effectue des transformations supplémentaires sur les données de l'étape **Silver** pour les enrichir, puis les sauvegarde au format Delta dans l'étape **Gold**.

Les fichiers CSV sont traités dans les répertoires suivants :
- **Bronze Path** : `../ds-bronze/`
- **Silver Path** : `../ds-silver/`
- **Gold Path** : `../ds-gold/`

## Prérequis

```bash
pip install deltalake
```

## Lancer le projet

```bash
cd scripts
```

Lancer le script qui convertit les données bronze en silver : 
```bash
python .\bronze_to_silver.py
```

Lancer le script qui convertit les données silver en gold : 
```bash
python .\silver_to_gold.py 
```

_Après ces 2 scripts lancés les données du dataset sont maintenant raffinées._