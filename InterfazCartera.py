from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PEDIDOS import *
from PRODUCTOS import *
from CLIENTES import *
from CARTERA import *
from InterfazCliente import *
from InterfazEmergenteProductosPedido import *
import InicioAdmin as ia


#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

class InterfazCartera():
	def __init__(self,ventana,tipo_inicio):
		self.inicio = tipo_inicio
		self.ventana = ventana
		self.ventana.title("P&C_DataBase - Cartera")
		self.ventana.configure(bg = DARKRED)
		self.marco1=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco1.grid(row=0,column=0,columnspan=4)

		self.boton3 = ttk.Button(ventana,text="Inicio",command=self.volver_inicio)
		self.boton3.place(x=0,y=0,width=70,height=30)

		#Lista de clientes
		c = Clientes()
		self.clientes = c.listar_clientes()
		self.cedulas = c.listar_cedulas()
		self.telefonos = c.listar_telefonos()

		#Añadir pedido
		etiqueta_nombre = Label(self.marco1,text="Información de cartera - Cuentas pendientes de pago",bg=DARKSALMON).grid(row=0,column=0,columnspan=3)


		#Mensaje
		self.mensaje=Label(text='',bg=DARKRED,fg='white')
		self.mensaje.place(x=100,y=100)

		#Tabla
		self.tabla=ttk.Treeview(self.ventana,columns=('#1','#2','#3', '#4'))
		self.tabla.grid(row=8,column=0,columnspan=5)
		self.tabla.heading('#0',text='Número de venta')
		self.tabla.heading('#1',text='Número pedido')
		self.tabla.heading('#2',text='Nombre cliente')
		self.tabla.heading('#3',text='Valor')
		self.tabla.heading('#4',text='Teléfono de contacto')

		self.mostrar_datos()


	def mostrar_datos(self):
		cartera = Cartera()
		datos = cartera.obtener_info()
		registros_actuales = self.tabla.get_children()
		nueva_tabla = []

		for dato in datos:
			indice = self.cedulas.index(dato[2])
			info = (dato[0], dato[1], self.clientes[indice], '$' + str(dato[3]),self.telefonos[indice])
			nueva_tabla.append(info)

		for registro in registros_actuales:
			self.tabla.delete(registro)

		for (id_venta,num_pedido,nombre,valor,telefono) in nueva_tabla:
			self.tabla.insert('',END,text=id_venta,values=(num_pedido,nombre,valor,telefono))

	def volver_inicio(self):
		self.ventana.destroy()
		ventana = Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('420x275')
		aplicacion = ia.Inicio(ventana,self.inicio)
		ventana.mainloop()

