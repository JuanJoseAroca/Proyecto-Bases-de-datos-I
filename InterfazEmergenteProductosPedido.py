from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PEDIDOS import *
from PRODUCTOS import *
from CLIENTES import *
from PRODUCTOS_PEDIDOS import *
from VENTAS import *

#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

class InterfazEmergente_productosPedidos():
	def __init__(self,ventana,cedula,num_pedido):
		self.ventana = ventana
		self.cedula = cedula
		self.pedido_nuevo = True
		self.num_pedido = num_pedido
		self.ventana.title("P&C_DataBase - Productos del pedido")
		self.ventana.configure(bg = MAROON)
		self.marco1=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco1.grid(row=0,column=1,columnspan=2)

		#Listas de productos, identificaciones y precios
		p = Productos()
		self.productos = p.listar_productos()
		self.ids = p.listar_ids()
		self.precios = p.listar_precios()

		#Selección del menú productos
		self.variable_p = StringVar(self.marco1)
		self.variable_p.set(self.productos[0])
		
		#Botón 1 (Añadir producto)
		self.boton1 = ttk.Button(self.marco1,text="Añadir",command=self.registrar_producto_en_pedido).grid(row=3,columnspan=3,sticky=W+E)

		#Etiqueta y entrada de la cantidad del mismo producto
		etiqueta_Cantidad = Label(self.marco1,text="Cantidad del producto",bg=DARKSALMON).grid(row=1,column=0)
		self.entrada_can_pedido = Entry(self.marco1)
		self.entrada_can_pedido.grid(row=1,column=1)

		#Menú desplegable productos
		etiqueta_producto = Label(self.marco1,text="Seleccionar producto",bg=DARKSALMON).grid(row=0,column=0)
		self.opcion_productos = OptionMenu(self.marco1,self.variable_p,*self.productos)
		self.opcion_productos.grid(row=0,column=1,columnspan=2)

		#Mensaje1
		self.mensaje1=Label(text='',bg=DARKRED,fg='white')
		self.mensaje1.grid(row=4,column=0,columnspan=3)

		#Tabla
		self.tabla=ttk.Treeview(self.ventana,columns=('#1','#2'))
		self.tabla.grid(row=7,column=0,columnspan=4)
		self.tabla.heading('#0',text='Producto')
		self.tabla.heading('#1',text='Cantidad')
		self.tabla.heading('#2',text='Valor')

	def registrar_producto_en_pedido(self):
		producto = self.variable_p.get()
		cantidad = self.entrada_can_pedido.get()
		if cantidad == '':
			messagebox.showerror(message='Por favor introduzca una cantidad del producto',title='Producto sin cantidad')
		else:
			cantidad = int(cantidad)
			producto_pedido = Productos_pedidos()
			indice = self.productos.index(producto)
			id_producto = self.ids[indice]
			valor = self.precios[indice]
			valor *= cantidad

			if self.pedido_nuevo == True:
				self.registrar_pedido(valor)
			else:
				self.actualizar_valor_pedido(valor)

			info_producto_pedido = (id_producto,self.num_pedido,cantidad,valor)
			producto_pedido.registrar(info_producto_pedido)
			self.mostrar_productos_pedido()
			self.pedido_nuevo = False

	def registrar_pedido(self,valor):
		registro = messagebox.askyesno(message='¿Está segur@ que desea agregar este pedido?, a partir de que se añada el primer producto no se podrá borrar',title='Añadir pedido')
		if registro:
			pedido = Pedidos()
			info_pedido = (self.cedula, 'Pendiente', valor)
			pedido.registrar(info_pedido)
			cliente = Clientes()
			cliente.adicionar_compra(self.cedula)
			info_venta = (self.num_pedido,self.cedula,valor,'Pendiente')
			venta = Ventas()
			venta.registrar(info_venta)


	def actualizar_valor_pedido(self,valor):
		pedido = Pedidos()
		pedido.actualizar_valor(self.num_pedido, valor)
		venta = Ventas()
		venta.actualizar_valor(self.num_pedido,valor)	

	def mostrar_productos_pedido(self):
		pp = Productos_pedidos()
		datos = pp.obtener_producto_pedido(self.num_pedido)
		registros_actuales = self.tabla.get_children()
		nueva_tabla = []
		for dato in datos:
			info = (self.productos[dato[1]-1], dato[3], '$' + str(dato[4]))
			nueva_tabla.append(info)
		for registro in registros_actuales:
			self.tabla.delete(registro)
		for (pro, cant, val) in nueva_tabla:
			self.tabla.insert('',END,text=pro,values=(cant,val))
			
