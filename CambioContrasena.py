from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from USUARIOS import *
import CambioContrasena as cc
import InterfazAcceso as iacc


#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'
LIGTHSEAGREEN = '#20B2AA'

class MenuCambioCon():
	def __init__(self,ventana):
		self.ventana=ventana
		self.ventana.title("P&C_DataBase - Actualización de la contraseña")
		usuarios = [
		'',
		'Administrador',
		'Propietario'
		]
		marco1=LabelFrame(self.ventana,bg=DARKRED,fg='white')
		marco1.grid(row=2,column=5,columnspan=5)
		marco1.place(x=55,y=193)
		

		self.variable = StringVar(ventana)
		self.variable.set(usuarios[0])

		#Menú desplegable
		etiqueta_menu = Label(marco1,text="Tipo de usuario",bg=DARKRED,fg='white').grid(row=0,column=2)
		self.opcion = OptionMenu(marco1,self.variable,*usuarios)
		self.opcion.grid(row=0,column=3,columnspan=2)

		#Contraseña actual
		etiqueta_contraseña_actual = Label(marco1,text="Contraseña actual",bg=DARKRED,fg='white').grid(row=1,column=2)
		self.contraseña_actual = Entry(marco1, show='*')
		self.contraseña_actual.grid(row=1,column=3)
		self.contraseña_actual.focus()

		#Contraseña nueva
		etiqueta_contraseña_nueva = Label(marco1,text="Nueva Contraseña",bg=DARKRED,fg='white').grid(row=2,column=2)
		self.contraseña_nueva = Entry(marco1, show='*')
		self.contraseña_nueva.grid(row=2,column=3)
		self.contraseña_nueva.focus()

		#Botón 1 (Validar contraseña)
		self.boton1 = ttk.Button(marco1,text="Validar",command=self.cambiar)
		self.boton1.grid(row=4,column=2,columnspan=2,sticky=W+E)

		#Botón de volver al acceso
		self.boton1 = Button(self.ventana,text="Volver",command=self.volver_acceso,bg=DARKRED,fg='white')
		self.boton1.place(x=0,y=0)

	def cambiar(self):
		actual = self.contraseña_actual.get()
		nueva = self.contraseña_nueva.get()
		tipo_usuario = self.variable.get()
		usuario = Usuarios()
		mensaje = usuario.cambiar_contrasena(tipo_usuario,actual,nueva)
		messagebox.showinfo(message=mensaje, title='Cambio de contraseña')

	def volver_acceso(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = '#8B0000')
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('325x320')
		logo = PhotoImage(file="Logo.png")
		fondo = Label(ventana,image=logo).place(x=0,y=0)

		aplicacion = iacc.Login(ventana)

		ventana.mainloop()		