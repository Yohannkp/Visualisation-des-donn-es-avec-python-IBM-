# Résumé du Projet : Analyse des Incendies Historiques

## Introduction
Ce projet vise à analyser les données historiques des incendies en Australie en utilisant des outils de visualisation et d'analyse de données. Les données proviennent de [ce lien](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv).

---

## Étapes Réalisées

### 1. Chargement et Préparation des Données
- Les données ont été chargées dans un DataFrame Pandas depuis l'URL fournie.
- Conversion de la colonne `Date` en type datetime.
- Extraction des colonnes `Year` et `Month` à partir de la colonne `Date`.

**Illustration :** Aperçu des premières lignes du DataFrame.

---

### 2. Analyse des Données
#### a. Types de Données
- Vérification des types de données pour s'assurer de leur cohérence.

#### b. Moyenne de la Surface des Incendies par Année
- Calcul de la moyenne de la surface estimée des incendies par année.
- Visualisation de la tendance annuelle.

**Illustration :** Graphique en ligne montrant la moyenne des surfaces estimées par année.

#### c. Moyenne de la Surface des Incendies par Mois
- Calcul de la moyenne de la surface estimée des incendies par mois et par année.
- Visualisation des données pour les années 2010 à 2013.

**Illustration :** Graphique en barres empilées pour les années 2010-2013.

---

### 3. Analyse Régionale
#### a. Moyenne de la Luminosité des Incendies par Région
- Calcul de la luminosité moyenne estimée des incendies pour chaque région.
- Visualisation avec un graphique en barres.

**Illustration :** Graphique en barres montrant la luminosité moyenne par région.

#### b. Répartition des Pixels d'Incendies par Région
- Calcul de la somme des pixels d'incendies pour chaque région.
- Visualisation avec un diagramme circulaire.

**Illustration :** Diagramme circulaire montrant la répartition des pixels d'incendies.

---

### 4. Distribution et Corrélations
#### a. Histogramme de la Luminosité Moyenne
- Visualisation de la distribution de la luminosité moyenne estimée des incendies.

**Illustration :** Histogramme de la luminosité moyenne.

#### b. Distribution par Région
- Visualisation de la distribution de la luminosité moyenne par région à l'aide de KDE et d'histogrammes empilés.

**Illustration :** Graphiques KDE et histogrammes empilés.

#### c. Corrélation entre Puissance Radiative et Confiance
- Création d'un nuage de points pour visualiser la relation entre la puissance radiative moyenne et la confiance moyenne.

**Illustration :** Nuage de points montrant la corrélation.

---

### 5. Cartographie
#### a. Carte des Régions
- Création d'une carte interactive avec Folium pour localiser les régions australiennes.

**Illustration :** Carte interactive des régions.

#### b. Visualisation des Incendies par Région
- Ajout de marqueurs circulaires pour représenter les incendies sur une carte.

**Illustration :** Carte avec marqueurs circulaires.

---

## Conclusion
Ce projet a permis d'explorer les données historiques des incendies en Australie, de visualiser les tendances et de mieux comprendre les dynamiques régionales et temporelles des incendies. Les visualisations interactives et les analyses statistiques offrent des perspectives utiles pour la gestion des incendies et la prise de décision.