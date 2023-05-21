import pandas as pd
from sklearn.datasets import load_iris

d = load_iris()
X, Y = d.data, d.target

# Créer le DataFrame à partir de X
df = pd.DataFrame(X)

# Ajouter la colonne "groundtruth" à partir de Y
df = df.assign(groundtruth=Y)

# Afficher le nombre de lignes et de colonnes
nombre_lignes, nombre_colonnes = df.shape
print("Nombre de lignes :", nombre_lignes)
print("Nombre de colonnes :", nombre_colonnes)

# Filtrer les lignes correspondant au type "setosa"
setosa_df = df.loc[df['groundtruth'] == 0]

# Afficher les lignes correspondantes à "setosa"
print(setosa_df)

# Regrouper les données par type de plante
grouped_df = df.groupby('groundtruth')

# Afficher les groupes
for group_name, group_data in grouped_df:
    print("Type de plante :", group_name)
    print(group_data)
    print()

# Afficher le DataFrame
print(df)

# Créer un nouveau DataFrame pour stocker les statistiques
stats_df = pd.DataFrame(columns=['Type', 'Max', 'Min', 'Moyenne', 'Ecart-type'])

# Calculer les statistiques pour chaque groupe
for group_name, group_data in grouped_df:
    stats = {
        'Type': group_name,
        'Max': group_data.max(),
        'Min': group_data.min(),
        'Moyenne': group_data.mean(),
        'Ecart-type': group_data.std()
    }
    stats_df = stats_df.append(stats, ignore_index=True)

# Afficher le nouveau DataFrame avec les statistiques
print(stats_df)
