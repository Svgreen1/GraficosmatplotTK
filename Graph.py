import pandas as pd
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import messagebox   ##libreria ventanas emergentes
from tkinter import filedialog  
import datetime
import numpy as np
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from matplotlib import pyplot
import sqlalchemy
from sqlalchemy import create_engine

#libro = "C:\\Users\\Sebastian_Valverde\\Desktop\\Excel\\servi.xlsx"
df = pd.read_excel(libro, header=0, delim_whitespace=True)
#engine= sqlalchemy.create_engine("mysql+pymysql://root:svalverde1@localhost:3306/servi")  #/credenciales de ingreso
#df=pd.read_sql_table("variable", engine)
tabla = df[["media", "humedad", "temperatura", "fechahora"]]
tX=tabla.get("fechahora") #.astype(str)
aY=tabla.get("temperatura")
bY=tabla.get("humedad")
cY=tabla.get("media")

class raiz(Tk):
    def __init__(self):     #crear objetos para raiz
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
        #fondo=PhotoImage(file="uniajclogo.png")
        #fondoimagen=Label(self, image=fondo).place(x=0,y=0)
        #slider=Scale(self,label="Dato de tiempo", orient='horizontal', variable=z, from_=z[0], to=(len(z)-164), command=valor1, length=400).pack()
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
        #toolbar=NavigationToolbar2Tk(a,self)
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
        #interact(tX, i=1)
        toolbar = NavigationToolbar2Tk(canvas, self).pack(side=LEFT)
def valor1(valor):
    seleccion = "valor = " +str(valor)
    print(seleccion)
def emergente():
    messagebox.showinfo("Agradecimientos", "Agradecimientos a ")
print(k)
root = raiz()
root.mainloop()

