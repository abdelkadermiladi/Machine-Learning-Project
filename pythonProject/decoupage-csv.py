import pandas as pd
# Load the data into a pandas DataFrame
df = pd.read_csv('df2-SeanceUnique.csv')

df['date'] = pd.to_datetime(df['date'])
#avril_rows = df[df['date'].dt.month == 4]

#start_date = pd.Timestamp('2022-10-31')
#end_date = pd.Timestamp('2022-10-31')
#start_date = pd.Timestamp(start_date)
#end_date = pd.Timestamp(end_date)

#extracted = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
#extracted = extracted.sort_values(by='date')
#extracted.to_csv('df2-10_31.csv', index=False)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

# Extraire les lignes où la date est égale à '2022-10-31'
df_jourmax = df[df['date'].dt.date == pd.to_datetime('2022-04-03').date()]

# Afficher le dataframe résultant
df_jourmax.to_csv('df2_DimancheMinCumul.csv', index=False)