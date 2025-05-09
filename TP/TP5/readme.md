# Analyse des données d'immigration au Canada (1980 - 2013)

## Introduction
Ce notebook explore les données d'immigration au Canada entre 1980 et 2013. Les analyses incluent des visualisations pour mieux comprendre les tendances et les distributions des immigrants par pays, continent et années.

---

## Chargement et préparation des données
- Les données ont été chargées depuis un fichier CSV et stockées dans un DataFrame `df_can`.
- Les colonnes inutiles ont été supprimées, et l'index a été défini sur la colonne `Country`.
- Une colonne `Total` a été ajoutée pour calculer le total des immigrants par pays sur toutes les années.

---

## Exploration des données
### Dimensions et aperçu des données
- Dimensions des données : `(196, 39)`
- Les premières lignes du DataFrame ont été affichées pour un aperçu rapide.

### Extraction des années
- Une liste `years` contenant les années de 1980 à 2013 a été créée pour faciliter les analyses.

---

## Visualisations des tendances globales
### Immigration totale au Canada (1980 - 2013)
- Un graphique en ligne a été tracé pour montrer l'évolution du total des immigrants au fil des années.
- **Illustration :** *(Insérer ici le graphique de la cellule 4)*

### Distribution des immigrants par année
- Une somme annuelle des immigrants a été calculée et visualisée à l'aide d'un graphique en ligne.
- **Illustration :** *(Insérer ici le graphique de la cellule 6)*

---

## Analyse par pays
### Immigration depuis Haïti
- Les données pour Haïti ont été extraites et visualisées pour montrer les tendances spécifiques.
- **Illustration :** *(Insérer ici le graphique de la cellule 10)*

### Top 5 des pays contributeurs
- Les 5 pays ayant le plus contribué à l'immigration ont été identifiés et visualisés à l'aide d'un graphique en barres.
- **Illustration :** *(Insérer ici le graphique de la cellule 16)*

### 5 pays avec le moins d'immigrants
- Les 5 pays ayant le moins contribué à l'immigration ont été identifiés et visualisés.
- **Illustration :** *(Insérer ici le graphique de la cellule 17)*

---

## Analyse par continent
### Répartition continentale
- Les données ont été regroupées par continent pour analyser la répartition des immigrants.
- Un graphique en secteurs a été utilisé pour visualiser cette répartition.
- **Illustration :** *(Insérer ici le graphique de la cellule 27)*

---

## Comparaisons spécifiques
### Chine vs Inde (2000 - 2013)
- Les données pour la Chine et l'Inde ont été extraites et comparées sur la période 2000-2013.
- **Illustration :** *(Insérer ici le graphique de la cellule 23)*

### Danemark, Norvège et Suède (1980 - 2013)
- Les données pour ces trois pays ont été extraites et visualisées pour analyser les tendances.
- **Illustration :** *(Insérer ici le graphique de la cellule 22)*

---

## Distribution des immigrants
### Histogrammes
- Des histogrammes ont été tracés pour analyser la distribution des immigrants par année et par pays.
- **Illustration :** *(Insérer ici les graphiques des cellules 18 et 20)*

---

## Subplots et visualisations combinées
- Plusieurs sous-graphiques ont été créés pour combiner différentes visualisations dans une seule figure.
- **Illustration :** *(Insérer ici les graphiques des cellules 28, 29 et 30)*

---

## Conclusion
Ce notebook fournit une analyse approfondie des tendances d'immigration au Canada entre 1980 et 2013. Les visualisations permettent de mieux comprendre les contributions des différents pays et continents, ainsi que les variations au fil des années.
