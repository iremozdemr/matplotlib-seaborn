import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)

#basic graph (plt.plot)

x = [1,2,3,4]
y = [2,4,6,8]

plt.plot(x, y, label="2x", linestyle="--", linewidth=5, color="pink", marker=".",markersize=10)
#label çizginin ne çizgisi olduğunu gösterir
#linestyle çizgiyi sürekli yerine çizgili yapar
#linewidth çizginin kalınlığını gösterir
#color çizginin rengini gösterir
#marker çizgideki noktaları gösterir
#markersize çizgideki noktaların büyüklüğünü gösterir

#plt.plot([1,2,3,4],[2,4,6,8])

plt.suptitle("my first graph")
#büyük başlık
plt.title("graph1")
#küçük başlık

plt.xlabel("x axis!")
#x ekseninin başlığı
plt.ylabel("y axis!")
#y ekseninin başlığı

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])

x2 = np.arange(0,4,0.5)
y2 = x2**2
print(x2)
print(y2)
plt.plot(x2,y2,label="x^2")
#ikinci çizgiyi ekleme

plt.legend()
#labelin gösterilmesi için yazılması zorunlu

plt.grid()
#grafiği kareli hale getirir
#default olarak axis="both"

#plt.grid(axis="x",linestyle="--",color="pink")
#dikey çizgileri değiştirir
#plt.grid(axis="y",linestyle="--",color="green")
#yatay çizgileri değiştirir

plt.savefig("myfirstgraph.png")
#grafiği kodun bulunduğu dosyaya kaydeder

plt.show()