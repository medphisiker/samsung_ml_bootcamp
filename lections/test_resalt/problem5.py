import numpy as np
import pandas as pd

df = pd.read_csv('lections\\test_resalt\\input5.csv')

# подготовка таблицы
df.drop('Unnamed: 0', axis=1, inplace=True)
df['max_val'] = df.max(axis=1)

# сбор статистики
max_counts = []
for col in df.columns[:-1]:
    max_counts.append((df[col] == df['max_val']).sum())

print(np.argmax(max_counts))
