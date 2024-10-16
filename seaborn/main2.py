import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

df = sns.load_dataset("tips")
df.head()

sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()