# Projet Fracture numérique — Accès Internet et PIB par habitant

Étude de la fracture numérique à travers 5 pays (Sénégal, Nigeria, France, États-Unis, Chine) : évolution du taux d'accès à Internet et corrélation avec le PIB par habitant, à partir de l'API de la Banque mondiale.

## Données
- **Source** : API World Bank (`api.worldbank.org`)
- **Indicateurs utilisés** :
  - `IT.NET.USER.ZS` — Individuals using the Internet (% of population)
  - `NY.GDP.PCAP.CD` — GDP per capita (current US$)
- **Pays** : Sénégal (SN), Nigeria (NG), France (FR), États-Unis (US), Chine (CN)
- **Période** : 1960-2025

## Contenu du notebook
1. **Récupération des données** — appels API pour les deux indicateurs (accès Internet et PIB par habitant)
2. **Nettoyage** — extraction des champs imbriqués (`country`, `indicator`), conversion de `date` en entier
3. **Analyse temporelle** — évolution du taux d'accès à Internet par pays (Seaborn, `lineplot`)
4. **Fusion** — jointure interne (`merge how='inner'`) des deux jeux de données sur `country` et `date`
5. **Corrélation** — calcul de la corrélation entre taux d'accès à Internet et PIB par habitant

## Technologies
- Python, pandas
- Requests (appels API)
- Seaborn

## Installation
```bash
pip install pandas requests seaborn
```

## Résultats principaux
- Trajectoires d'adoption d'Internet très différentes selon les pays : États-Unis et France dépassent 85-90 % dès 2020, la Chine ne franchit ce seuil qu'en 2023-2024, tandis que le Sénégal et le Nigeria restent en retrait (40-60 % en 2023-2024)
- Corrélation forte (0,72) entre taux d'accès à Internet et PIB par habitant
- La fracture numérique reste étroitement liée au niveau de développement économique, sans que cela n'établisse de lien de causalité direct

## Auteur
Projet réalisé dans le cadre d'un exercice d'analyse de données.