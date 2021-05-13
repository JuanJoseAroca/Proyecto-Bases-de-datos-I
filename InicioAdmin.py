from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import InterfazCliente as iclien
import InterfazPedido as iped
import InterfazVentas as iv
import InterfazProveedor as ipv
import InterfazEstadisticas as ie
import InterfazCartera as ca
import InterfazIngredientes as ii
import InterfazProducto as ipro
import InterfazAcceso as iacc


#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

class Inicio():
	def __init__(self,ventana,tipo_inicio):
		self.tipo_inicio = tipo_inicio
		self.ventana = ventana
		self.ventana.title("P&C_DataBase - Inicio")
		self.ventana.configure(bg = DARKRED)
		self.marco1=LabelFrame(self.ventana,bg=DARKSALMON)

		#Mensaje
		self.mensaje=Label(text='',bg=DARKRED,fg='white', font=('Times new roman', 14))
		self.mensaje.place(x=15,y=0)
		self.mensaje['text'] = 'Elija el tipo de información a la que desea acceder'

		#Botón 1 (Clientes)
		self.boton1 = ttk.Button(self.ventana,text="Clientes",command=self.abrir_clientes)
		self.boton1.place(x=0,y=40,width=200,height=50)

		#Botón 2 (Pedidos)
		self.boton2 = ttk.Button(self.ventana,text="Pedidos",command=self.abrir_pedidos)
		self.boton2.place(x=210,y=40,width=200,height=50)

		#Botón 3 (Ventas)
		self.boton3 = ttk.Button(self.ventana,text="Ventas",command=self.abrir_ventas)
		self.boton3.place(x=0,y=100,width=200,height=50)

		#Botón 4 (proveedores)
		self.boton4 = ttk.Button(self.ventana,text="Proveedores",command=self.abrir_proveedores)
		self.boton4.place(x=210,y=100,width=200,height=50)

		if self.tipo_inicio == 'Administrador':
			#Botón 5 (Estadísticas)
			self.boton5 = ttk.Button(self.ventana,text="Estadísticas",command=self.abrir_estadisticas)
			self.boton5.place(x=0,y=160,width=200,height=50)
			#Botón 6 (Cartera)
			self.boton6 = ttk.Button(self.ventana,text="Cartera",command=self.abrir_cartera)
			self.boton6.place(x=210,y=160,width=200,height=50)
		else:
			#Botón 7 (Ingredientes)
			self.boton7 = ttk.Button(self.ventana,text="Ingredientes",command=self.abrir_ingredientes)
			self.boton7.place(x=0,y=160,width=200,height=50)
			#Botón 8 (Productos)
			self.boton8 = ttk.Button(self.ventana,text="Productos",command=self.abrir_productos)
			self.boton8.place(x=210,y=160,width=200,height=50)

		#Botón 9 (Regreso al acceso)
		self.boton9 = ttk.Button(self.ventana,text="Cerrar sesión",command=self.abrir_acceso)
		self.boton9.place(x=105,y=220,width=200,height=50)	

			
	def abrir_clientes(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		aplicacion = iclien.InterfazCliente(ventana,self.tipo_inicio)
		ventana.mainloop()

	def abrir_pedidos(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		aplicacion = iped.InterfazPedido(ventana,self.tipo_inicio)
		ventana.mainloop()

	def abrir_ventas(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		aplicacion = iv.InterfazVenta(ventana,self.tipo_inicio)
		ventana.mainloop()

	def abrir_proveedores(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		aplicacion = ipv.InterfazProveedor(ventana,self.tipo_inicio)
		ventana.mainloop()

	def abrir_estadisticas(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('455x240')
		aplicacion = ie.InterfazEst(ventana,self.tipo_inicio)
		ventana.mainloop()

	def abrir_cartera(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('980x200')
		aplicacion = ca.InterfazCartera(ventana,self.tipo_inicio)
		ventana.mainloop()

	def abrir_ingredientes(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		aplicacion = ii.InterfazIngrediente(ventana,self.tipo_inicio)
		ventana.mainloop()

	def abrir_productos(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		aplicacion = ipro.InterfazProducto(ventana,self.tipo_inicio)
		ventana.mainloop()	
	
	def abrir_acceso(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = '#8B0000')
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('325x320')
		logo = PhotoImage(file="Logo.png")
		fondo = Label(ventana,image=logo).place(x=0,y=0)

		aplicacion = iacc.Login(ventana)

		ventana.mainloop()		

		

	
