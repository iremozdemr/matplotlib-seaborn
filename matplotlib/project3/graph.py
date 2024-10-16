import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3,4,5]
y = [3,7,0,1,4]
z = [5,7,1,2,9]

plt.figure(1)
axes = plt.axes(projection="3d")
axes.scatter(x,y,z)
axes.set_title("my graph1")
axes.set_xlabel("x axes")
axes.set_ylabel("y axes")
axes.set_zlabel("z axes")

plt.figure(2)
axes = plt.axes(projection="3d")
axes.plot(x,y,z)
axes.set_title("my graph2")
axes.set_xlabel("x axes")
axes.set_ylabel("y axes")
axes.set_zlabel("z axes")

plt.show()