# Projet dans le cadre du cours Interfaces web pour le TAL

##  Objectif du projet

Ce projet a pour objectif de développer une interface web permettant d'analyser le sentiment de textes saisis par l'utilisateur ou provenant d'un fichier .txt. L'analyse est basée sur l'outil _TextBlob_, qui permet de classifier un texte comme positif, neutre ou négatif.

## Description du système

L'application web permet aux utilisateurs :
- D'entrer un texte manuellement et d'obtenir son analyse de sentiment.
- De téléverser un fichier `.txt` contenant plusieurs lignes de texte pour une analyse en masse.
- De visualiser la répartition des sentiments sous forme de graphique généré dynamiquement.
- D'explorer les résultats classés sous différentes onglets : Positif, Neutre et Négatif.

## Technologies et outils utilisés

- **Backend** : FastAPI
- **Frontend** : HTML, CSS, Bootstrap
- **Analyse des sentiments** : TextBlob
- **Visualisation des résultats** : Matplotlib, Seaborn
- **Gestion des templates** : Jinja2

## Structure

- `main.py` - Backend FastAPI
- `index.html` - Interface utilisateur
- `js.js` - Code JavaScript

## Installation et exécution

### Installation

1. Cloner le répertoire
    ```bash
   git clone git@github.com:agataskrzyniarz1/sentiment_analysis_API.git
    ```
2. Naviguer vers le répertoire du projet
    ```bash
    cd sentiment_analysis_API
    ```
3. Installer les dépendances
    ```bash
    pip install -r requirements.txt
    ```

### Exécution

```bash
uvicorn main:app --reload
```
Ensuite, ouvrez **http://127.0.0.1:8000/** dans votre navigateur.

#### Auteur : Agata Skrzyniarz