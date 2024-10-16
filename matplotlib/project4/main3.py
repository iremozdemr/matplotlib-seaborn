import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

x = np.array([2,4,6,8,10])
y = np.array([1,3,5,7,9])

plt.plot(x,y)
plt.show()

plt.plot(x)
plt.plot(y)
plt.show()