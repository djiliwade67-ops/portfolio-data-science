# Projet Netflix — Analyse exploratoire

Analyse exploratoire du catalogue Netflix (`netflix_titles.csv`, 8 807 titres) : nettoyage des données, tendances d'ajout par année et par pays de production.

## Données
- **Source** : `netflix_titles.csv`
- **12 colonnes** : `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`

## Contenu du notebook
1. **Exploration** — structure du dataset, valeurs manquantes (`.info()`, `.describe()`)
2. **Nettoyage**
   - `director`, `cast`, `country` → imputés par `"Unknown"`
   - `date_added`, `rating`, `duration` → imputés par le mode
   - `date_added` converti en `datetime`, extraction de `year_added` / `month_added`
3. **Analyse temporelle** — évolution du nombre de titres ajoutés par année (Plotly : courbe + barres)
4. **Analyse géographique** — top 10 des pays producteurs (Seaborn)
5. **Croisement pays × année** — table pivot + heatmap

## Technologies
- Python, pandas
- Matplotlib, Seaborn, Plotly

## Installation
```bash
pip install pandas matplotlib seaborn plotly
```

## Résultats principaux
- Croissance forte des ajouts entre 2015 et 2019 (pic à 2 016 titres), puis léger recul en 2020-2021
- États-Unis et Inde dominent largement le catalogue
- Diversification progressive vers d'autres pays (Corée du Sud, Japon) sur les années récentes

## Fichiers générés
- `netflix_ajouts_par_annee.html` — graphique interactif Plotly

## Auteur
Projet réalisé dans le cadre d'un exercice d'analyse de données.