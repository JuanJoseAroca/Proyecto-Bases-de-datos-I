from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PEDIDOS import *
from PRODUCTOS import *
from CLIENTES import *
from VENTAS import *
from PRODUCTOS_PEDIDOS import *

#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'
CORNISILK = '#FFF8DC'

class InterfazEmergente_Factura():
	def __init__(self,ventana,num_pedido):
		self.ventana = ventana
		self.num_pedido = num_pedido
		self.ventana.title("P&C_DataBase - Productos del pedido")
		self.ventana.configure(bg = MAROON)

		cliente = Clientes()
		self.cedula_cliente = cliente.cedula_en_pedido(self.num_pedido)
		clientes = cliente.listar_clientes() 
		cedulas = cliente.listar_cedulas()
		self.nombre_cliente = clientes[cedulas.index(self.cedula_cliente)]

		etiqueta_nombre = Label(self.ventana,text="Nombre del cliente: " + self.nombre_cliente,bg=CORNISILK).grid(row=0,column=0)
		etiqueta_cedula = Label(self.ventana,text="Cédula del cliente: " + str(self.cedula_cliente),bg=CORNISILK).grid(row=1,column=0)


		#Listas de productos, identificaciones y precios
		p = Productos()
		self.productos = p.listar_productos()
		self.ids = p.listar_ids()
		self.precios = p.listar_precios()


		#Tabla
		self.tabla=ttk.Treeview(self.ventana,columns=('#1','#2'))
		self.tabla.grid(row=7,column=0,columnspan=4)
		self.tabla.heading('#0',text='Producto')
		self.tabla.heading('#1',text='Cantidad')
		self.tabla.heading('#2',text='Valor')

		self.mostrar_productos_pedido()

	def mostrar_productos_pedido(self):
		pp = Productos_pedidos()
		datos = pp.obtener_producto_pedido(self.num_pedido)
		registros_actuales = self.tabla.get_children()
		nueva_tabla = []
		valor_total_pedido = 0
		for dato in datos:
			info = (self.productos[dato[1]-1], dato[3], '$' + str(dato[4]))
			nueva_tabla.append(info)
			valor_total_pedido += dato[4]
		for registro in registros_actuales:
			self.tabla.delete(registro)
		for (pro, cant, val) in nueva_tabla:
			self.tabla.insert('',END,text=pro,values=(cant,val))

		self.tabla.insert('',END,text='Valor total',values=('','$' + str(valor_total_pedido)))	


