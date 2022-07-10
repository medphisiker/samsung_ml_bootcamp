import numpy as np
import pandas as pd

df = pd.read_csv('lections\\test_pandas\input3.csv')
print(bool(df.isna().sum().sum()))
