#pandas support(поддерживает) форматы csv, exel, sql, html and others
import pandas as pd

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])

#save df csv
df.to_csv('CountryList.csv', sep='|')
print(df)

#read df csv
dfRead = pd.read_csv('CountryList.csv', sep='|')
print(dfRead)

#save df excel (для этого нужно установить 'pip install openpyxl')
#writer = pd.ExcelWriter('output.xlsx')
#df.to_excel(writer)
#writer.save()

