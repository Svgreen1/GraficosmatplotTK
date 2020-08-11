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
#$$$$$$$$$$$$$$lectura exel
libro = "C:\\Users\\Sebastian_Valverde\\Desktop\\Excel\\servi.xlsx"
df = pd.read_excel(libro, header=0, delim_whitespace=True)


###$###
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
#y=[11,12,11,11,14,14,14,15,15,15,15,16,16,16,16,18,18,18,18,18,18,18,23,23,23,23,26,26,26,26,26,27,27,27,27,27,27,28,28,28,28,28,30,30,30,30,32,32,
#33,33,33,31,31,31,31,31,30,30,30,30,30,28,28,28,28,28,28,25,25,25,25,25,25,25,25,24,24,24,24,24,24,22,22,22,22,22,20,20,20,20,17,17,17,17,17,17,17,
#13,13,13,13,13,13,11,11,11,11,11,11,11,11,11,14,14,14,15,15,15,15,16,16,16,16,18,18,18,18,18,18,18,23,23,23,23,26,26,26,26,26,27,27,27,27,27,27,28,28,28,28,28,30,30,30,30,32,32,
#33,33,33,31,31]
#x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,
#52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,
#125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161]
