import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.arange(20).reshape(4, 5),
                  columns=list('abcde'))
print(df)
df['f'] = df['a'] + df['b'] + df['c'] + df['d'] + df['e']
print(df)
