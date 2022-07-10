import numpy as np
import pandas as pd

df = pd.read_csv('lections\\test_resalt\\input4.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)

res = 0
for col in df.columns:
    res += (df[col] == 1).sum()
    
print(res)
