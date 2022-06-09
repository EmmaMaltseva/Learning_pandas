import pandas as pd
df = pd.DataFrame({
    'country': ['USA', 'China', 'Russia', 'Japan'],
    'population': [301.7, 1442, 143, 125.4 ],
    'square': [9826675, 9596961, 17125191, 377975]
})
print(df)
print(type(df['square']))

