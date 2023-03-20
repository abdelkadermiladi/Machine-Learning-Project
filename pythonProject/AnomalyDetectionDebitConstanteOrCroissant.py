import pandas as pd

# Lire le fichier CSV contenant les données mesurées
df = pd.read_csv("df2-10.csv", parse_dates=["date"])

# Définir la période de temps pendant laquelle la consommation doit augmenter progressivement
periode_croissance = pd.Timedelta(minutes=30)

# Boucler sur les mesures de débit pour détecter les anomalies
for i in range(len(df)):
    # Vérifier si la mesure de débit est non nulle
    if df.loc[i, "debit"] != 0:
        # Trouver la période de temps pendant laquelle la consommation augmente progressivement
        debut_croissance = df.loc[i, "date"]
        fin_croissance = debut_croissance + periode_croissance
        debit_initial = df.loc[i, "debit"]
        j = i + 1
        while j < len(df) and df.loc[j, "debit"] >= debit_initial and df.loc[j, "date"] <= fin_croissance:
            debit_initial = df.loc[j, "debit"]
            j += 1
        # Si la période de temps est égale à la période de croissance, c'est une anomalie
        if j - i == periode_croissance.total_seconds() / 30:
            print(f"Anomalie détectée au niveau du débit entre {debut_croissance} et {fin_croissance}")
