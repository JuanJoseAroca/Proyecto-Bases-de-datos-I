import InterfazAcceso as iacc
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
							
		
if __name__=="__main__":
    ventana=Tk()
    ventana.configure(bg = '#8B0000')
    ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
    ventana.geometry('325x320')
    logo = PhotoImage(file="Logo.png")
    fondo = Label(ventana,image=logo).place(x=0,y=0)

    aplicacion = iacc.Login(ventana)

    ventana.mainloop()
