import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#aynı pencerede grafik oluşturma

figure,axis = plt.subplots(2,2)

x1 = [1,2,3]
y1 = [2,4,6]
axis[0,0].plot(x1,y1)

x2 = [1,2,3]
y2 = [2,4,6]
axis[0,1].scatter(x2,y2)

plt.show()