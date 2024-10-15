import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#basic graph (plt.scatter)

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([1,7,24,13,2,4,6,9])
#iki array de kesinlikle aynı uzunluğa sahip olmalıdır

plt.scatter(x,y)
#grafikteki (x,y) noktalarını işaretler

plt.suptitle("my second graph")
plt.title("graph2")

plt.savefig("mysecondgraph.png")

plt.show()