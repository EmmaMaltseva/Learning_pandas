import pandas as pd

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])
print(df)
df.index.name = 'Country Code'
print(df[['population', 'square']])
print(df.loc['KZ':'BY', :])

#Фильтрование DataFrame

print(df[df.population > 10][['country', 'square']])

#df.country or df['country] одно и то же
print(df.country)
print(df['country'])

#Delete indexes
print(df.reset_index())

df['density'] = df['population'] / df['square'] * 1000000
print(df)

# Delete column
del df['density']
print(df)

#Rename columns
df = df.reset_index()
df = df.rename(columns={'Country Code': 'country_code'})
print(df)
