from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PRODUCTOS import *
import InicioAdmin as ia

#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

# Interfaz de usuario
class InterfazProducto():
	def __init__(self,ventana,tipo_inicio):
		self.inicio = tipo_inicio
		self.ventana=ventana
		self.ventana.title("P&C_DataBase - Productos")
		marco1=LabelFrame(self.ventana,bg=DARKSALMON)
		marco1.grid(row=0,column=0,columnspan=2)
		marco2=LabelFrame(self.ventana,bg=DARKSALMON)
		marco2.grid(row=0,column=2,columnspan=2)
		#Nombre producto
		etiqueta_producto = Label(marco1,text="Producto",bg=DARKSALMON).grid(row=0,column=0)
		self.entrada_producto = Entry(marco1)
		self.entrada_producto.grid(row=0,column=1)
		self.entrada_producto.focus()

		#Precio producto
		etiqueta_precio = Label(marco1,text="Precio $",bg=DARKSALMON).grid(row=1,column=0)
		self.entrada_precio = Entry(marco1)
		self.entrada_precio.grid(row=1,column=1) 

		#Botón 1 (Añadir producto)
		boton1 = ttk.Button(marco1,text="Añadir producto").grid(row=3,columnspan=2,sticky=W+E)
		boton1 = ttk.Button(marco1,text="Añadir producto",command=self.ingresar_dato).grid(row=3,columnspan=2,sticky=W+E)

		#Botón 2 (Mostrar productos)
		boton2 = ttk.Button(marco2,text="Mostrar todos los productos").grid(row=3,columnspan=2,sticky=W+E)
		boton2 = ttk.Button(marco2,text="Mostrar todos los productos",command=self.mostrar_datos).grid(row=3,columnspan=2,sticky=W+E)

		#Botón Inicio
		self.boton4 = ttk.Button(ventana,text="Inicio",command=self.volver_inicio)
		self.boton4.place(x=0,y=0,width=50,height=30)
		
		#Tabla
		self.tabla=ttk.Treeview(self.ventana,columns=('#1','#2'))
		self.tabla.grid(row=7,column=0,columnspan=4)
		self.tabla.heading('#0',text='ID')
		self.tabla.heading('#1',text='Producto')
		self.tabla.heading('#2',text='Precio')

	def mostrar_datos(self):
		productos = Productos()
		nueva_tabla = productos.obtener_tabla()
		registros_actuales = self.tabla.get_children()

		for registro in registros_actuales:
			self.tabla.delete(registro)

		for  (id_producto, producto, precio) in nueva_tabla:
			self.tabla.insert('',END,text=id_producto,values=(producto, '$'+str(precio)))


	def ingresar_dato(self):
		if len(self.entrada_producto.get()) > 0 and len(self.entrada_precio.get()) > 0:
			producto = Productos()

			if (producto.existe(self.entrada_producto.get())):
				messagebox.showerror(message='El producto ingresado ya se encuentra en la base datos',title='Producto anteriormente registrado')
				
			else:
				info = (self.entrada_producto.get(), int(self.entrada_precio.get()))
				producto.registrar(info)
		else:
			messagebox.showwarning(message='Debe ingresar los datos del producto',title='Datos no válidos')

	def volver_inicio(self):
		self.ventana.destroy()
		ventana = Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('420x275')
		aplicacion = ia.Inicio(ventana,self.inicio)
		ventana.mainloop()		
	