import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("df2-SeanceUnique.csv")

# Convertir la colonne "date" en objet datetime
df["date"] = pd.to_datetime(df["date"])

# Ajouter une colonne "debitcumule" qui calcule le débit cumulé par jour
df["debitcumule"] = df.groupby(df["date"].dt.date)["debit"].cumsum()

# Trouver la date qui correspond au débit cumulé maximal et minimal pour chaque jour de la semaine
max_debitcumule_par_jour = df.groupby(df["date"].dt.weekday)["debitcumule"].idxmax()
dates_max_debitcumule_par_jour = df.loc[max_debitcumule_par_jour]["date"].dt.date

min_debitcumule_par_jour = df.groupby(df["date"].dt.weekday)["debitcumule"].idxmin()
dates_min_debitcumule_par_jour = df.loc[min_debitcumule_par_jour]["date"].dt.date


# Afficher les résultats
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for i, date_max_debitcumule in enumerate(dates_max_debitcumule_par_jour):
    jour_max_debitcumule = jours[i]
    print(f"Le jour correspondant au max débit cumulé pour {jour_max_debitcumule} est {date_max_debitcumule}")

print("\n")

for i, date_min_debitcumule in enumerate(dates_min_debitcumule_par_jour):
    jour_min_debitcumule = jours[i]
    print(f"Le jour correspondant au min débit cumulé pour {jour_min_debitcumule} est {date_min_debitcumule}")

