import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

#plot 1
x = np.array([2,4,6,8,10])
y = np.array([1,3,5,7,9])
plt.subplot(1,3,1)
plt.title("1")
plt.plot(x,y)

#plot 2
x = np.array([5,13,23,56,88])
y = np.array([1,0,5,7,10])
plt.subplot(1,3,2)
plt.title("2")
plt.plot(x,y)

#plot 3
x = np.array([20,13,25,56,88])
y = np.array([1,0,5,7,10])
plt.subplot(1,3,3)
plt.title("3")
plt.plot(x,y)

plt.show()