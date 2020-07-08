from tkinter import *  
from tkinter import messagebox   ##libreria ventanas emergentes
from tkinter import filedialog 

raiz=Tk() #raiz var interfaz


def emergente():
    messagebox.showinfo("Agradecimientos", "Agradecimientos Uniajc, Honorable profesora Erika Sarria")

def aviso():
    valor=messagebox.askokcancel("Salir", "¿desea salir del monitor?")
    if valor==True:  ##aceptar=true
        raiz.destroy()  ##cerrar

def abrirexcel():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="excel tesis:", filetypes=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto","*.txt")))
    #######funcion de busqueda archivo"""""""""""""""""""""""""""""""""""""""""""""""""""""


raiz.title("Monitor de variables")
raiz.resizable(True,True) #reminensionar x,y
raiz.geometry("1200x670") #size  el tamaño se acopla al frame
raiz.iconbitmap("icono1.ico") ##icono ventana

fondo=PhotoImage(file="uniajclogo.png")
fondoimagen=Label(raiz, image=fondo).place(x=0,y=0)
raiz.config(bg="#f8f9fe") #background
##menú################################################
barramenu=Menu(raiz)
raiz.config(menu=barramenu)

archivomenu=Menu(barramenu, tearoff=0)
archivomenu.add_command(label="Reiniciar")
archivomenu.add_separator()
archivomenu.add_command(label="salir", command=aviso)

herramientamenu=Menu(barramenu, tearoff=0)
herramientamenu.add_command(label="Ejecurar archivo xlsx", command=abrirexcel)

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label="Acerca de...", command=emergente)

barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Herramientas", menu=herramientamenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)

##frameee         1''''''''''''''''''''''''''''''''''''''''''''
frame1=Frame()
frame1.pack()
frame1.config(bg="black")
frame1.config(width="400", height="300" )  #x,y
frame1.config(bd=7) ##borde
frame1.config(relief="groove")
frame1.config(cursor="hand2")
#frame 2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
frame2=Frame()
frame2.pack(side="left")
frame2.config(bg="black")
frame2.config(width="400", height="350" )  #x,y
frame2.config(bd=7) ##borde
frame2.config(relief="groove")
frame2.config(cursor="hand2")
#frame 3"""""""""""""""""""""""""""""""""""""""""""""""""""""
frame3=Frame()
frame3.pack(side="right")
frame3.config(bg="black")
frame3.config(width="400", height="350" )  #x,y
frame3.config(bd=7) ##borde
frame3.config(relief="groove")
frame3.config(cursor="hand2")
###################################################
raiz.mainloop()
