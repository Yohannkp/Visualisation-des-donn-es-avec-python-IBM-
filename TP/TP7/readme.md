# Rapport détaillé du TP : Visualisation de données géographiques avec Folium et Pandas

## Introduction
Ce TP a pour objectif d'explorer et de visualiser des données géographiques en utilisant les bibliothèques Python **Folium** et **Pandas**. Nous avons manipulé des jeux de données variés pour créer des cartes interactives et des visualisations impactantes. Ce document détaille les étapes réalisées, les concepts abordés, et laisse des emplacements pour insérer des illustrations pertinentes pour une présentation.

---

## Étapes réalisées

### 1. Importation des bibliothèques nécessaires
Nous avons importé les bibliothèques **Pandas**, **NumPy**, et **Folium** pour manipuler les données et créer des cartes interactives.

```python
import numpy as np
import pandas as pd
import folium
```

---

### 2. Création de cartes de base
#### Carte mondiale par défaut
Une carte mondiale simple a été créée avec **Folium**.

```python
world_map = folium.Map()
world_map
```

**Illustration suggérée :** Capture d'écran de la carte mondiale par défaut.

#### Carte centrée sur le Canada
Nous avons centré la carte sur le Canada avec un niveau de zoom faible.

```python
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
world_map
```

**Illustration suggérée :** Carte centrée sur le Canada avec un zoom faible.

---

### 3. Exploration des styles de cartes
Nous avons exploré différents styles de cartes, tels que **Cartodb dark_matter** et **Cartodb positron**.

```python
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Cartodb dark_matter')
world_map
```

**Illustration suggérée :** Comparaison entre les styles de cartes.

---

### 4. Cartographie de données géographiques spécifiques
#### Carte centrée sur le Mexique
Nous avons défini les coordonnées géographiques du Mexique et créé une carte centrée sur ce pays.

```python
mexico_latitude = 23.6345
mexico_longitude = -102.5528
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=6, tiles='Cartodb positron')
mexico_map
```

**Illustration suggérée :** Carte centrée sur le Mexique.

---

### 5. Visualisation des incidents à San Francisco
#### Chargement des données
Nous avons chargé un jeu de données contenant des incidents de police à San Francisco.

```python
df_incidents = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')
```

#### Création d'une carte de San Francisco
Une carte centrée sur San Francisco a été créée.

```python
latitude = 37.77
longitude = -122.42
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)
sanfran_map
```

**Illustration suggérée :** Carte de San Francisco.

#### Ajout de marqueurs pour les incidents
Nous avons ajouté des marqueurs pour visualiser les 100 premiers incidents.

```python
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.vector_layers.CircleMarker(
        [lat, lng],
        radius=5,
        color='yellow',
        fill=True,
        popup=label,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(sanfran_map)
sanfran_map
```

**Illustration suggérée :** Carte avec des marqueurs pour les incidents.

#### Utilisation de clusters
Nous avons regroupé les incidents en clusters pour une meilleure lisibilité.

```python
from folium import plugins
incidents = plugins.MarkerCluster().add_to(sanfran_map)
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(location=[lat, lng], popup=label).add_to(incidents)
sanfran_map
```

**Illustration suggérée :** Carte avec des clusters.

---

### 6. Visualisation des données d'immigration au Canada
#### Chargement des données
Nous avons chargé un jeu de données sur l'immigration au Canada.

```python
df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
```

#### Création d'une carte choroplèthe
Une carte choroplèthe a été générée pour visualiser l'immigration totale par pays.

```python
world_geo = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json'
folium.Choropleth(
    geo_data=world_geo,
    data=df_can,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Total Immigration to Canada (1980-2013)'
).add_to(world_map)
world_map
```

**Illustration suggérée :** Carte choroplèthe montrant l'immigration au Canada.

---

## Conclusion
Ce TP a permis de manipuler des données géographiques et de les visualiser de manière interactive avec **Folium**. Les cartes générées offrent une vue d'ensemble des données et permettent une analyse visuelle efficace. Les emplacements suggérés pour les illustrations peuvent être utilisés pour enrichir une présentation et rendre les résultats plus impactants.