import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

ages = []
for x in range(100):
    ages.append(random.randint(0,100))
#0 ve 100 arasında 100 tane sayı üretir

plt.hist(ages,rwidth=0.7)
#rwidth sütunların arasındaki boşluk miktarını ayarlar

plt.show()