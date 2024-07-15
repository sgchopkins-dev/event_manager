from database.db import get_data, get_active, countdown

df = get_data()
df['Action'] = df.apply(lambda row: get_active(row), axis=1)
df = df[df['Action'] == 'Action']
df['Weeks'] = df.apply(lambda row: countdown(row)[0], axis=1)
df['Days'] = df.apply(lambda row: countdown(row)[1], axis=1)
cols = ['Event', 'Weeks', 'Days']
df = df.loc[:, cols]
print(df)
