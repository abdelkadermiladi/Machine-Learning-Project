import pandas as pd
# Load both files into separate DataFrames
df2 = pd.read_csv("MaxCumulSeanceUnique\df_LundiMaxCumul.csv")
df3 = pd.read_csv("MaxCumulSeanceUnique\df_MardiMaxCumul.csv")
df4 = pd.read_csv("MaxCumulSeanceUnique\df_MercrediMaxCumul.csv")
df5 = pd.read_csv("MaxCumulSeanceUnique\df_JeudiMaxCumul.csv")
df6 = pd.read_csv("MaxCumulSeanceUnique\df_VendrediMaxCumul.csv")
df7 = pd.read_csv("MaxCumulSeanceUnique\df_SamediMaxCumul.csv")
df8 = pd.read_csv("MaxCumulSeanceUnique\df_DimancheMaxCumul.csv")

#dfjuin = pd.read_csv("df2-6.csv")
#dfjuillet = pd.read_csv("df2-7.csv")
# Find the index of the row where you want to insert the new data
#insert_index = march_rows[march_rows['date'] == '2022-03-05 05:13:54'].index[0]

# Concatenate the two DataFrames together
#result = pd.concat([march_rows.iloc[:insert_index], hi_data, march_rows.iloc[insert_index:]])
result = pd.concat([df6,df7,df8,df2, df3,df4,df5, df6,df7,df8,df2, df3,df4,df5, df6,df7,df8,df2, df3,df4,df5, df6,df7,df8,df2, df3,df4,df5, df6,df7,df8,df2, df3,df4,df5, df6,df7,df8,df2, df3,df4,df5, df6,df7,df8,df2, df3,df4,df5, df6,df7,df8,df2, df3,df4,df5, df6,df7,df8,df2, df3,df4])
# Write the result to a new CSV file
#result=pd.concat([dfjuin,dfjuillet])
result.to_csv("concatJoursJuilletAoutMAX.csv", index=False)

