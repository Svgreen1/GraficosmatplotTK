import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111)

def animate(i):
    libro = "C:\\Users\\Sebastian_Valverde\\Desktop\\Excel\\servi.xlsx"
    df = pd.read_excel(libro, header=0, delim_whitespace=True)
    tabla = df[["temperatura", "fechahora"]]
    x=tabla.get("fechahora") 
    y=tabla.get("temperatura")
    xs = []
    ys = []
    
    xs.append(x)
    ys.append(y)
    
       
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

