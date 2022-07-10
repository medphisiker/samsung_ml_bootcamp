import numpy as np
import pandas as pd

df = pd.read_csv('lections\\test_pandas\\input4.csv')
corr = df.corr().drop('Unnamed: 0').drop('Unnamed: 0', axis=1)
corr = corr.abs().max(axis=0)
print(corr.tolist())
