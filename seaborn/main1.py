import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()

#matplotlib ile görselleştirme
df["sex"].value_counts().plot(kind="bar")
plt.show()

#seaborn ile görselleştirme
sns.countplot(x=df["sex"],data=df)
plt.show()