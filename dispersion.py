import pandas as pd

data = {'Name': ['Anna', 'Ben', None, 'Daisy', None],
        'Score': [90, 85, None, 88, None]}
df = pd.DataFrame(data)

print("Before:")
print(df)

df.fillna(method='ffill', inplace=True)

print("\nAfter forward fill:")
print(df)
