import pandas as pd

# Charger les données depuis le fichier CSV
data = pd.read_csv("CSVfiles/df2-SeanceUnique.csv")

# Convertir la colonne "date" en datetime
data["date"] = pd.to_datetime(data["date"])

# Définir une fonction pour détecter les anomalies
def detecter_anomalies(row):

    # Vérifier si la période est "nuit" ou "soir"
    if row["date"].hour < 6 or row["date"].hour >= 21:
        # Si le débit est non nul, c'est une anomalie
        if row["debit"] != 0:
            return row["date"], "anomalie de consommation hors horaire de travail"

    # Vérifier si la période est "matin" ou "apres-midi"
    else:
        # Si le débit dépasse 4.5, c'est une anomalie
        if row["debit"] > 4.5:
            return row["date"], "anomalie de consommation excessive"

    # Si aucun des critères ci-dessus n'est rempli, il n'y a pas d'anomalie
    return None, None
#Appliquer la fonction "detecter_anomalies" à chaque ligne du DataFrame
anomalies = data.apply(detecter_anomalies, axis=1)
k=0
#Afficher les résultats
for date, type_anomalie in anomalies:
    if (date!=None) & (type_anomalie != None ):
        k=k+1
        print(f"Anomalie de consommation détectée le {date} : {type_anomalie}")
if k==0:
    print("Pas d'anomalie de consommation détectée")