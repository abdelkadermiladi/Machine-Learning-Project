import pandas as pd

# Charger le premier fichier CSV
df1 = pd.read_csv('JuinJuillet.csv')

# Extraire la colonne "date"
dates = df1['date']

# Charger le deuxième fichier CSV
df2 = pd.read_csv('concatJoursJuilletAoutMAX.csv')

# Remplacer les valeurs de la colonne "debit" par celles du deuxième fichier
df1['debit'] = df2['debit']

# Enregistrer le résultat dans un nouveau fichier CSV
df1.to_csv('JuinJuilletMaxCumul.csv', index=False)
