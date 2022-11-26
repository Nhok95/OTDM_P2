import pandas as pd
import numpy as np

df = pd.read_csv("ionosphere.data", header=None)

df.columns = [str(i) for i in df.columns]
df.loc[df["34"]== "g", "34"] = 1
df.loc[df["34"] == "b", "34"] = -1

np.savetxt(r'ionosphere.txt', df, fmt='%.3f')
