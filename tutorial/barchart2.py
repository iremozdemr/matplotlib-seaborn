import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

labels=["a","b","c"]
values=[1,12,5]

bars = plt.bar(labels,values)
bars[0].set_hatch("/")
bars[1].set_hatch("o")
bars[2].set_hatch("*")
#sütunların içini tarar

plt.show()