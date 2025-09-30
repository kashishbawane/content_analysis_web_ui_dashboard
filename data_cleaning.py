import pandas as pd

# If you kept Excel
df = pd.read_excel("dataset.xlsx")

# If you saved it as CSV
# df = pd.read_csv("dataset.csv")

# Cleaning steps
df['Release_Year'] = df['Release_Year'].fillna(0)
df['Certificate'] = df['Certificate'].replace({
    'Not Rated': 'Unrated',
    'Passed': 'Approved',
    '16': '16+',
    '13': '13+',
    '18': '18+',
    'All': 'UA',
    '15': '15+',
    '12': '12+',
    'U/A': 'UA'
})
df['Duration'] = df['Duration'].fillna(0)
df['Genre'] = df['Genre'].fillna('Not Available')
df['Director'] = df['Director'].fillna('Not Available')
df['Cast'] = df['Cast'].fillna('Not Available')
