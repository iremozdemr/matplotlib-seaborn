import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)

#basic graph (plt.plot)

x = [1,2,3,4]
y = [2,4,6,8]

plt.plot(x, y, label="2x", linestyle="--", linewidth=5, color="pink", marker=".",markersize=10)
#label cizginin ne cizgisi oldugunu gosterir
#linestyle cizgiyi surekli yerine cizgili yapar
#linewidth cizginin kalinligini gosterir
#color cizginin rengini gosterir
#marker cizgideki noktaları gosterir
#markersize cizgideki noktaların buyuklugunu gosterir

#plt.plot([1,2,3,4],[2,4,6,8])

plt.suptitle("my first graph")
#buyuk baslik
plt.title("graph1")
#kucuk baslik

plt.xlabel("x axis!")
#x ekseninin basligi
plt.ylabel("y axis!")
#y ekseninin basligi

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])

x2 = np.arange(0,4,0.5)
y2 = x2**2
print(x2)
print(y2)
plt.plot(x2,y2,label="x^2")
#ikinci cizgiyi ekleme

plt.legend()
#labelin gosterilmesi icin yazilmasi zorunlu

plt.grid()
#grafigi kareli hale getirir
#default olarak axis="both"

#plt.grid(axis="x",linestyle="--",color="pink")
#dikey cizgileri degistirir
#plt.grid(axis="y",linestyle="--",color="green")
#yatay cizgileri degistirir

plt.savefig("myfirstgraph.png")
#grafigi kodun bulundugu dosyaya kaydeder

plt.show()