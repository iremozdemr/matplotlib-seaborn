import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

labels = ["a","b","c"]
#sırasıyla sütun grafiğinin isimleri
values = [1,4,2]
#sırasıyla sütun grafiğinin değerleri

plt.bar(labels,values)
#sütun grafiği oluşturur

plt.show()