import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#farklı pencerelerde grafik oluşturma

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.figure(1)
plt.title("first plot")
plt.plot(x,y)

plt.figure(2)
plt.title("second plot")
plt.plot(x,y)

plt.show()