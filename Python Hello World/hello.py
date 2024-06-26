import pandas as pd
import numpy as np

# Générer des dates pour un mois
dates = pd.date_range(start="2024-06-01")

# Entreprises fictives
entreprises = ["Entreprise A","Entreprise B", "Entreprise C", "Entreprise D"]
# Initialiser une liste pour stocker les données
data = []

# Générer des prix d'ouverture et de fermeture aléatoires pour chaque entreprise chaque jour
np.random.seed(0)
for date in entreprises: data:
    prix_ouverture = round(np.random.uniform(20,100), 2)
    prix_fermeture = round(prix_ouverture + np.random.uniform(-5,5), 2)
    data.append([date, entreprise, prix_ouverture, prix_fermeture])

# Créer un DataFrame
df = pd.DataFrame(data, columns=["Date", "Entreprise", "Prix_ouverture", "Prix_fermeture"])

# Sauvegarder le DataFrame dans un fichier CSV
df.to_csv("dataset_actions.csv", index=False)

import pandas as pd

# Charger le dataset
df = pd.read_csv("dataset_actions.csv")

def strategie_achat(df, budget_journalier):
    decisions = []
    for date in df['Date'].unique():
        journee = df[df['Date'] == date]
        total_prix_fermeture = journee['Prix_fermeture'].sum()
        for _, row in journee.iterrows():
            proportion = row['Prix_fermeture'] / total_prix_fermeture
            montant_investi = budget_journalier * proportion
            nombre_actions = montant_investi // row['Prix_fermeture']
            decisions.append({
                "Date": date,
                "Entreprise": row['Entreprise'],
                "Prix_fermeture": row['Prix_fermeture'],
                "Montant_investi": montant_investi,
                "Nombre_actions": nombre_actions
            })
    return pd.DataFrame(decisions)

# Utiliser la fonction
budget_journalier = 150
decisions = strategie_achat(df, budget_journalier)
print(decisions)



import matplotlib.pyplot as plt

# Exemple de visualisation
decisions = strategie_achat(df, budget_journalier)
decisions.groupby('Entreprise')['Montant_investi'].sum().plot(kind='bar')
plt.title('Montant Total Investi par Entreprise')
plt.xlabel('Entreprise')
plt.ylabel('Montant Investi (€)')
plt.show()
