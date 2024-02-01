import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

languages = ["python","c","c++","c#","java"]
votes = [21,54,26,78,12]

#plt.pie(votes,labels=languages)

plt.pie(votes,labels=languages,autopct="%.2f")

plt.show()