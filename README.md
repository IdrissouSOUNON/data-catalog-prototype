# 📊 Prototype de Catalogue de Données Publiques

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

## 🎯 Objectif

Ce projet propose un prototype de **catalogue de données publiques** visant à structurer, référencer et faciliter l’exploration de données issues de différentes structures administratives.

L’objectif est de répondre aux enjeux de :
- gouvernance des données
- réduction des silos informationnels
- amélioration de l’accès à l’information pour les décideurs et les développeurs

---

## 🧠 Contexte

Dans de nombreuses administrations, les données sont dispersées, hétérogènes et difficilement exploitables.

Ce prototype s’inscrit dans une logique de modernisation des systèmes d’information en permettant :
- une meilleure visibilité des données disponibles
- une standardisation des métadonnées
- une base pour le développement de plateformes Open Data

---

## ⚙️ Fonctionnalités

- 🔍 Scan automatique de fichiers de données (.csv, .xlsx)
- 🧾 Génération d’un catalogue structuré au format JSON
- 📊 Interface interactive de visualisation des datasets
- 🔎 Recherche et filtrage des données
- 🏷️ Ajout de métadonnées (source, description, type de données)

---

## 🧱 Architecture du projet

data-catalog-prototype/
│
├── data/
│ └── sample_datasets/
├── app.py
├── catalog.json
├── requirements.txt
└── README.md

---

## 🛠️ Technologies utilisées

- Python
- Streamlit
- JSON

---

## ▶️ Lancer le projet

### 1. Cloner le repository

```bash
git clone https://github.com/ton-username/data-catalog-prototype.git
cd data-catalog-prototype
