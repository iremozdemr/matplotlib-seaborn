import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts()

df["sex"].value_counts().plot(kind="bar")
plt.show()