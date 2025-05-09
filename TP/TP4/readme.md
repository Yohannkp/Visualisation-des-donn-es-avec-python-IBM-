# Résumé du Travail Réalisé

## Importation des Bibliothèques
- Importation des bibliothèques nécessaires : `numpy`, `pandas`, `matplotlib`.

---

## Chargement des Données
- Lecture des données d'immigration au Canada depuis un fichier CSV.
- Affichage des premières lignes pour un aperçu des données.

---

## Préparation des Données
- Définition de la colonne `Country` comme index.
- Création de sous-ensembles de données :
    - `df_continents` : Données regroupées par continent.
    - `df_top15` : Les 15 pays ayant le plus grand nombre d'immigrants.
    - `df_japan` : Données spécifiques au Japon.
    - `df_CI` : Données pour la Chine et l'Inde.
    - `df_total` : Total des immigrants par année.
    - `new_df` : Données regroupées par décennies (1980s, 1990s, 2000s).

---

## Visualisations Réalisées
1. **Diagrammes en Secteurs (Pie Charts)** :
     - Immigration par continent (1980-2013).
     - Utilisation de couleurs personnalisées et d'explosions pour certains segments.

     *(Illustration à insérer ici)*

2. **Diagrammes en Boîte (Box Plots)** :
     - Immigration japonaise (1980-2013).
     - Comparaison entre la Chine et l'Inde.
     - Immigration des 15 principaux pays par décennies.

     *(Illustration à insérer ici)*

3. **Graphiques en Nuage de Points (Scatter Plots)** :
     - Immigration totale au Canada (1980-2013) avec ligne de régression.
     - Immigration combinée du Danemark, de la Norvège et de la Suède.
     - Immigration du Brésil et de l'Argentine (normalisée).
     - Immigration de la Chine et de l'Inde (normalisée).

     *(Illustration à insérer ici)*

4. **Graphiques en Ligne (Line Plots)** :
     - Comparaison des tendances d'immigration pour la Chine et l'Inde.

     *(Illustration à insérer ici)*

5. **Graphiques Combinés** :
     - Diagramme en boîte et graphique en ligne pour la Chine et l'Inde.

     *(Illustration à insérer ici)*

---

## Analyse Statistique
- Calcul des statistiques descriptives pour les différents sous-ensembles de données.
- Normalisation des données pour certaines visualisations.

---

## Modélisation
- Ajustement d'une ligne de régression pour prédire les tendances d'immigration totale.

---

## Résultats Clés
- Les données montrent une augmentation générale de l'immigration au Canada entre 1980 et 2013.
- Les principaux contributeurs à l'immigration sont l'Inde, la Chine et les Philippines.
- Les tendances varient selon les pays et les continents.

---

*(Illustrations supplémentaires à insérer ici)*