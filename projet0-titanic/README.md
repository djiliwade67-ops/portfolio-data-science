# Titanic - Analyse exploratoire des données

## Contexte
Ce projet consiste en une analyse exploratoire du célèbre dataset Titanic (891 passagers), avec pour objectif d'identifier les facteurs qui ont influencé les chances de survie des passagers lors du naufrage. La question centrale : **quelles caractéristiques (sexe, classe sociale, âge, prix du billet...) sont associées à la survie ?**

## Pourquoi ce projet
Ce projet a été réalisé pour me familiariser avec les bases de la data science : manipulation de données avec Pandas, nettoyage d'un dataset réel (valeurs manquantes, doublons), et visualisation avec Seaborn/Matplotlib. C'est un projet d'introduction qui me permet de démontrer une démarche complète d'analyse exploratoire (EDA), de l'import des données jusqu'aux conclusions.

## Méthodologie
1. **Import des données** : chargement du dataset Titanic via `seaborn.load_dataset('titanic')`.
2. **Exploration initiale** : inspection des types, des statistiques descriptives et des valeurs manquantes (`.info()`, `.describe()`, `.isnull().sum()`).
3. **Nettoyage des données** :
   - Suppression des colonnes trop incomplètes ou redondantes (`deck`, `embark_town`).
   - Imputation des valeurs manquantes (`age` par la médiane, `embarked` par le mode).
   - Suppression des doublons.
   - Écriture d'une fonction `clean_titanic()` réutilisable pour automatiser ce pipeline de nettoyage.
4. **Visualisation** :
   - Boxplot de l'âge par classe.
   - Countplot de la survie par sexe.
   - Heatmap des corrélations entre variables numériques.
   - Pairplot âge/tarif coloré par survie.
5. **Synthèse** : calcul de statistiques agrégées (ex. tarif moyen payé selon la survie) et rédaction des conclusions.

## Résultats clés
1. **Classe et âge** : les passagers de 1ère classe sont en médiane plus âgés que ceux de 3ème classe.
2. **Sexe et survie** : les femmes ont un taux de survie nettement supérieur aux hommes.
3. **Facteurs les plus liés à la survie** : la classe (`pclass`, corrélation -0.33) et le prix du billet (`fare`, corrélation 0.25) sont les variables numériques les plus corrélées à la survie.
4. **Prix du billet et survie** : les survivants ont payé en moyenne 50€ contre 24€ pour les non-survivants, soit plus du double.

**Conclusion générale** : la survie sur le Titanic n'était pas aléatoire. Elle reflète des priorités d'évacuation (femmes/enfants d'abord) et des inégalités socio-économiques (accès privilégié aux canots pour les passagers de 1ère classe). Ces variables (sexe, classe, prix du billet) sont de bons candidats comme features pour un futur modèle de prédiction.

## Technologies utilisées
- Python
- Pandas
- Seaborn
- Matplotlib
- Jupyter Notebook

## Comment lancer ce projet
Le projet est disponible sur GitHub :https://github.com/djiliwade67-ops/portfolio-data-science

