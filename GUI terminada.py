from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from tkinter import messagebox, filedialog 
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
import time
import os
#---------LIBRERIAS

plt.style.use('ggplot')
fig = plt.Figure(figsize=(12, 6.5), dpi=94)



def animate(i):
    #libro = "servi111.xlsx" 
    #df = pd.read_excel(libro, header=0, delim_whitespace=True)
    try:
        engine= sqlalchemy.create_engine("mysql+pymysql://root:svalverde1@localhost:3306/servi")  #/credenciales de ingreso
        df=pd.read_sql_table("variable", engine)
        tabla = df[["media", "humedad", "temperatura", "fechahora"]]
        tX=tabla.get("fechahora") #.astype(str)
        aY=tabla.get("temperatura")
        bY=tabla.get("humedad")
        cY=tabla.get("media")
        ax.clear()
        ax.plot(tX, aY,color="yellow")
        ax.grid(True)
        ax.set_title("SISTEMA DE MONITOREO INALAMBRICO PARA CULTIVOS DE HORTALIZAS EN BUENOS AIRES (CAUCA)")
        ax.set_ylabel("Temperatura(°C)")
        ay.clear()
        ay.plot(tX, bY,color="green")
        ay.set_ylabel("  Humedad relativa(%)")
        ay.grid(True)
        az.clear()
        az.plot(tX, cY,color="red")
        az.grid(True)
        az.set_ylabel("Humedad del suelo")
    except ValueError:
        print("")

   # plt.pause(60)
    


root = Tk()
def emergente():
    messagebox.showinfo("Agradecimientos", "Agradecimientos honorable profesora Erika Sarria y a la UNIAJC")

def aviso():
    valor=messagebox.askokcancel("Salir", "¿desea salir del monitor?")
    if valor==True:  ##aceptar=true
        root.destroy()  ##cerrar
def abrir():
    os.startfile("Conexióncultivo.exe")
    #fichero=filedialog.askopenfilename(title="Abrir", initialdir="Escritorio:", filetypes=(("Ficheros de Aplicación", "*.exe"), ("Ficheros de texto","*.txt")))        

barramenu = Menu(root)
root.config(menu=barramenu)
ayudamenu=Menu(barramenu, tearoff=0)
archivomenu=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="Archivo", menu=archivomenu)
archivomenu.add_command(label="salir", command=aviso)
herramientamenu=Menu(barramenu, tearoff=0)
herramientamenu.add_command(label="establecer conexión online", command=abrir)
barramenu.add_cascade(label="Herramientas", menu=herramientamenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)
ayudamenu.add_command(label="Acerca de...", command=emergente)


root.title("Monitor de variables")
root.minsize(1100, 700)
root.resizable(False,False) 
root.iconbitmap("uni.ico")        
root.config(bd=25) ##borde
root.config(relief="groove")
root.config(bg="black")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=TOP, fill=X, expand=True)#.grid(column=0,row=1)
toolbar = NavigationToolbar2Tk(canvas, root).pack(side=LEFT)
ax = fig.add_subplot(311)
ay = fig.add_subplot(312)
az = fig.add_subplot(313)


ani = animation.FuncAnimation(fig, animate, interval=3000, blit=False, repeat_delay=9000)
root.mainloop()