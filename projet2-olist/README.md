# Projet Olist — Analyse des commandes e-commerce

Analyse exploratoire du dataset e-commerce brésilien Olist : fusion de plusieurs tables (commandes, clients, articles, paiements) et étude des corrélations entre variables numériques.

## Données
- **Source** : dataset Olist (Kaggle)
- **Fichiers utilisés** :
  - `olist_orders_dataset.csv`
  - `olist_customers_dataset.csv`
  - `olist_order_items_dataset.csv`
  - `olist_order_payments_dataset.csv`

## Contenu du notebook
1. **Chargement** — import des tables `orders`, `customers`, `items`, `payments`
2. **Fusion 1** — `orders` + `customers` (relation un-à-un, `how='left'` sur `customer_id`)
3. **Fusion 2** — + `items` (relation un-à-plusieurs sur `order_id`, une commande peut contenir plusieurs articles)
4. **Fusion 3** — + `payments` (relation un-à-plusieurs sur `order_id`, une commande peut être réglée en plusieurs paiements)
5. **Analyse par état** — prix moyen et répartition des statuts de commande par `customer_state` (pivot tables)
6. **Corrélations** — matrices de corrélation (`price`, `freight_value`, `payment_value`) et heatmaps Seaborn

## Technologies
- Python, pandas
- Matplotlib, Seaborn

## Installation
```bash
pip install pandas matplotlib seaborn
```

## Résultats principaux
- Les fusions un-à-plusieurs (items, payments) démultiplient les lignes : 99 441 → 113 425 → 118 434
- Corrélation forte entre `price` et `payment_value` (0,74)
- Corrélation modérée entre `price` et `freight_value` (0,41), plus faible entre `freight_value` et `payment_value` (0,37)

## Auteur
Projet réalisé dans le cadre d'un exercice d'analyse de données.