import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from networkx.algorithms.bipartite.basic import color

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

x = np.array([13,28,11,100])

plt.plot(x)
plt.show()

plt.plot(x,color="r")
plt.show()

plt.plot(x,marker="o")
plt.show()

plt.plot(x,marker="*")
plt.show()

plt.plot(x,linestyle="dashed")
plt.show()

plt.plot(x,linestyle="dotted")
plt.show()

plt.plot(x,linestyle="dashdot")
plt.show()