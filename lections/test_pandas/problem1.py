import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.arange(start=1, stop=21), columns=['data'])
df = df[(df['data'] > 1) & (df['data'] < 20)]
print(len(df))
