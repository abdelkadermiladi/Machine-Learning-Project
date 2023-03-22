import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df1 = pd.read_csv('JuinJuilletMaxCumul.csv',parse_dates=['date'])
df2 = pd.read_csv('JuinJuillet.csv',parse_dates=['date'])
df3 = pd.read_csv("JuinJuilletMinCumul.csv",parse_dates=['date'])
df1['date'] = pd.to_datetime(df1['date'])


plt.figure(figsize=(100, 10))
plt.plot(df1['date'], df1['cumul'], label='Max Cumul')
plt.plot(df1['date'], df2['cumul'], label='JuinJuillet Cumul')
plt.plot(df1['date'], df3['cumul'], label='Min Cumul')
plt.xlabel('Date')
plt.ylabel('cumul')
plt.title('Variation de debit de Juin et Juillet')
plt.legend()
plt.show()

