from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from textblob import TextBlob
import uvicorn
from fastapi.staticfiles import StaticFiles
import matplotlib.pyplot as plt
import os
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from collections import Counter
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

def analyze_sentiment(text: str) -> str:
    """Sentiment de retour : positif, neutre ou négatif."""
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positif"
    elif polarity < 0:
        return "Négatif"
    else:
        return "Neutre"
    
def create_sentiment_chart(file_results):
    """Crée un graphique du nombre d'opinions pour chaque sentiment et l'enregistre sous forme d'image PNG."""
    sentiment_counts = {"Positif": 0, "Neutre": 0, "Négatif": 0}

    for _, sentiment in file_results:
        sentiment_counts[sentiment] += 1

    labels = list(sentiment_counts.keys())
    sizes = list(sentiment_counts.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, sizes, color=['green', 'yellow', 'red'])
    plt.xlabel("Sentiment")
    plt.ylabel("Nombre d'opinions")
    plt.title("Répartition des sentiments")
    
    # Enregistrement du graphique dans le dossier statique
    chart_path = "static/sentiment_chart.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path

# Route principale : affiche la page d'accueil
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route pour analyser un texte soumis via un formulaire
@app.post("/analyze")
async def analyze(request: Request, text: str = Form(...)):
    result = analyze_sentiment(text)
    return templates.TemplateResponse("index.html", {"request": request, "text": text, "result": result})

# Route pour analyser un fichier texte téléchargé par l'utilisateur
@app.post("/analyze-file")
async def analyze_file(request: Request, file: UploadFile = File(...)):
    content = await file.read()
    opinions = content.decode("utf-8").strip().split("\n")
    file_results = [(opinion, analyze_sentiment(opinion)) for opinion in opinions if opinion.strip()]

    # Création d'un graphique basé sur les résultats
    chart_path = create_sentiment_chart(file_results)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "file_results": file_results,
        "chart_path": chart_path
    })

# Démarrage du FastAPI
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
