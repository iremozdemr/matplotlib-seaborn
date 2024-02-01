import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv("csv-files/gas_prices.csv")

print(gas)

print(gas.Year)
print(gas["Year"])
#gas.Year = gas["Year"]

print(gas.Year[0:7])
#0,1,2,3,4,5,6 yillarini bastirir

for country in gas:
    print(country)

plt.title("gas prices over time")

#plt.plot(gas.Year,gas.USA)
#plt.plot(gas.Year,gas.Canada)
#plt.plot(gas.Year,gas.France)
#tum yillarin verisini bastirir

plt.plot(gas.Year[0:7],gas.USA[0:7])
plt.plot(gas.Year[0:7],gas.Canada[0:7])
plt.plot(gas.Year[0:7],gas.France[0:7])
#ilk 7 yilin verisini bastirir

plt.show()