import pandas as pd
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import messagebox   ##libreria ventanas emergentes
from tkinter import filedialog 

libro = "C:\\Users\\Sebastian_Valverde\\Desktop\\Excel\\servi.xlsx"
df = pd.read_excel(libro, header=0, delim_whitespace=True)
tabla = df[["media", "humedad", "temperatura", "fechahora"]]

tX=tabla.get("fechahora")
aY=tabla.get("temperatura")
bY=tabla.get("humedad")
cY=tabla.get("media")

class raiz(Tk):
    def __init__(self):
        super(raiz, self).__init__()
        self.title("Monitor de variables")
        self.minsize(1200, 670)
        self.matplotCanvas()
        self.iconbitmap("icono1.ico")         
        barramenu=Menu(self)
        self.config(menu=barramenu)
        self.config(bd=25) ##borde
        self.config(relief="groove")
        self.config(bg="black")
        slider=Scale(self,label="Tiempo", orient='horizontal').pack() ##slider para variable tiempo(datetime) 
        ayudamenu=Menu(barramenu, tearoff=0)
        ayudamenu.add_command(label="Acerca de...", command=emergente)
        barramenu.add_cascade(label="Ayuda", menu=ayudamenu)


    def matplotCanvas(self):
        #primer grafico................
        f = Figure(figsize=(11, 7), dpi=80) #pulgadas, Dots per inches dpi
        a = f.add_subplot(311)
        a.plot(tX,aY, color="yellow")
        a.grid(True)
        a.set_ylabel("°C Temperatura")
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        ##segundo<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        g = Figure(figsize=(11, 7), dpi=100)
        b = f.add_subplot(312)
        b.plot(tX, bY, color="green")
        b.grid(True)
        b.set_ylabel("% Humedad relativa")
        canvas2 = FigureCanvasTkAgg(g, self)
        canvas2.draw()
        #tercero<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        h = Figure(figsize=(11, 7), dpi=100)
        c = f.add_subplot(313)
        c.plot(tX, cY, color="red")
        c.grid(True)
        c.set_xlabel("Tiempo")
        c.set_ylabel("% humedad de suelo")
        canvas3 = FigureCanvasTkAgg(h, self)
        canvas3.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=X, expand=True)
    
def emergente():
    messagebox.showinfo("Agradecimientos", "Agradecimientos ")

root = raiz()
root.mainloop()
#print(tX.head())
