from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PEDIDOS import *
from PRODUCTOS import *
from CLIENTES import *
from VENTAS import *
import InterfazCliente as icli
from InterfazEmergenteProductosPedido import *
import InicioAdmin as ia



#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

class InterfazPedido():
	def __init__(self,ventana,tipo_inicio):
		self.ventana = ventana
		self.inicio = tipo_inicio
		self.ventana.title("P&C_DataBase - Pedidos")
		self.ventana.configure(bg = DARKRED)
		self.marco1=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco1.grid(row=0,column=0,columnspan=3)
		self.marco2=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco2.grid(row=0,column=2,columnspan=2)
		self.marco3=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco3.grid(row=0,column=4,columnspan=2)
		
		#Lista de clientes
		c = Clientes()
		self.clientes = c.listar_clientes()
		self.cedulas = c.listar_cedulas()

		#Lista de estados del pedido
		estados_pedido = [
		'Pendiente',
		'En proceso',
		'Entregado']

		#Selección menú desplegable clientes
		self.variable_c = StringVar(self.marco1)
		self.variable_c.set(self.clientes[0])

		#Selección menú desplegable estado de pedido
		self.variable_e = StringVar(self.marco3)
		self.variable_e.set(estados_pedido[0]) 

		#Añadir pedido
		etiqueta_nuevo_pedido = Label(self.marco1,text="Nuevo pedido",bg=DARKSALMON).grid(row=0,column=0)

		#Busqueda de cliente
		etiqueta_buscar_cliente = Label(self.marco2,text="Cédula cliente",bg=DARKSALMON).grid(row=1,column=0)
		self.entrada_cedula_cliente = Entry(self.marco2)
		self.entrada_cedula_cliente.grid(row=1,column=1)

		#Cambiar estado del pedido
		etiqueta_id_pedido = Label(self.marco3,text="Número del pedido",bg=DARKSALMON).grid(row=0,column=0)
		self.entrada_id_pedido = Entry(self.marco3)
		self.entrada_id_pedido.grid(row=0,column=1)

		#Botón 1 (Añadir pedido)
		self.boton1 = ttk.Button(self.marco1,text="Añadir pedido",command=self.abrir_ventana_productos_pedido).grid(row=5,columnspan=3,sticky=W+E)

		#Botón 2 (Buscar pedidos de un cliente)
		self.boton2 = ttk.Button(self.marco2,text="Buscar pedidos del cliente",command=self.buscar_pedidos).grid(row=2,columnspan=2,sticky=W+E)

		#Botón 3 (Mostrar todos los pedidos)
		self.boton3 = ttk.Button(self.marco2,text="Mostrar todos los pedidos",command=self.mostrar_datos).grid(row=3,columnspan=2,sticky=W+E)

		#Botón 4 (añadir cliente)
		self.boton4 = ttk.Button(self.marco1,text="Añadir nuevo cliente",command=self.abrir_interfaz_cliente).grid(row=4,columnspan=3,sticky=W+E)

		#Botón Inicio       
		self.boton5 = ttk.Button(ventana,text="Inicio",command=self.volver_inicio)
		self.boton5.place(x=0,y=0,width=100,height=30)

		#Botón actualizar
		self.boton6 = ttk.Button(ventana,text="Actualizar",command=self.actualizar)
		self.boton6.place(x=0,y=35,width=100,height=30)

		#Botón 7 (Actualizar pedido)
		self.boton7 = ttk.Button(self.marco3,text="Actualizar estado del pedido",command=self.modificar_estado_pedido).grid(row=4,columnspan=3,sticky=W+E)

		#Botón 8 (Ver/Añadir productos del pedido)
		self.boton8 = ttk.Button(self.marco3,text="Ver/Añadir productos en pedido",command=self.actualizar_pedido).grid(row=5,columnspan=3,sticky=W+E)
		
		#Menú desplegable (Clientes)
		etiqueta_menu1 = Label(self.marco1,text="Seleccionar cliente",bg=DARKSALMON).grid(row=3,column=0)
		self.opcion_clientes = OptionMenu(self.marco1,self.variable_c,*self.clientes)
		self.opcion_clientes.grid(row=3,column=1,columnspan=2)

		#Menú desplegable (Estados pedidos)
		etiqueta_menu2 = Label(self.marco3,text="Seleccionar estado pedido",bg=DARKSALMON).grid(row=1,column=0)
		self.opcion_estados = OptionMenu(self.marco3,self.variable_e,*estados_pedido)
		self.opcion_estados.grid(row=1,column=1,columnspan=2)

		#Mensaje
		self.mensaje=Label(text='',bg=DARKRED,fg='white')
		self.mensaje.place(x=100,y=100)

		#Tabla
		self.tabla=ttk.Treeview(self.ventana,columns=('#1','#2','#3','#4'))
		self.tabla.grid(row=8,column=0,columnspan=5)
		self.tabla.heading('#0',text='Número de pedido')
		self.tabla.heading('#1',text='Nombre cliente')
		self.tabla.heading('#2',text='Valor del pedido')
		self.tabla.heading('#3',text='Estado del pedido')
		self.tabla.heading('#4',text='Estado del pago')

		self.mostrar_datos() 

	def abrir_ventana_productos_pedido(self):
		indice = self.clientes.index(self.variable_c.get())
		cedula = self.cedulas[indice]
		info = (cedula,'Pendiente')
		pedido = Pedidos()
		num_pedido = pedido.obtener_numero_pedido()
		ventana_eme = Tk()
		ventana_eme.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana_emergente = InterfazEmergente_productosPedidos(ventana_eme,cedula,num_pedido)
		ventana_eme.mainloop()

	def abrir_interfaz_cliente(self):
		ventana_clientes = Tk()
		ventana_clientes.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		emergente = icli.InterfazCliente(ventana_clientes,self.inicio)
		ventana_clientes.mainloop()

	def actualizar(self):
		c = Clientes()
		self.clientes = c.listar_clientes()
		self.cedulas = c.listar_cedulas()
		self.opcion_clientes = OptionMenu(self.marco1,self.variable_c,*self.clientes)
		self.opcion_clientes.grid(row=3,column=1,columnspan=2)
		self.mostrar_datos()

	def mostrar_datos(self):
		pedido = Pedidos()
		datos = pedido.obtener_tabla()
		registros_actuales = self.tabla.get_children()
		nueva_tabla = []
		venta = Ventas()

		for dato in datos:
			indice = self.cedulas.index(dato[1])
			info = (dato[0], self.clientes[indice], '$' + str(dato[3]), dato[2], venta.obtener_estado(dato[0]))
			nueva_tabla.append(info)

		for registro in registros_actuales:
			self.tabla.delete(registro)

		for (num,nombre,val,estado,est_pago) in nueva_tabla:
			self.tabla.insert('',END,text=num,values=(nombre,val,estado,est_pago))

	def modificar_estado_pedido(self):
		

		if len(self.entrada_id_pedido.get()) == 0:
			messagebox.showwarning(message='Debe introducir un ID de pedido',title='ID vacío')
		else:
			nuevo_estado = self.variable_e.get()
			id_pedido = int(self.entrada_id_pedido.get())
			pedido = Pedidos()

			if (pedido.existe(id_pedido)):
				pedido.actualizar_estado(nuevo_estado,id_pedido)
				self.mostrar_datos()
			else:
				messagebox.showerror(message='ID de pedido no está registrado en la base de datos',title='ID no registrado')	

	def buscar_pedidos(self):

		if len(self.entrada_cedula_cliente.get()) == 0:
			messagebox.showwarning(message='Debe introducir la cédula de un cliente para buscar sus pedidos',title='Cédula vacía')
		else:
			
			pedidos = Pedidos()
			cedula = int(self.entrada_cedula_cliente.get())

			if pedidos.existe_pedidos_cliente(cedula):
				datos = pedidos.buscar(cedula)
				registros_actuales = self.tabla.get_children()
				nueva_tabla = []

				for dato in datos:
					indice = self.cedulas.index(dato[1])
					info = (dato[0], self.clientes[indice], '$' + str(dato[3]), dato[2], 'Pendiente')
					nueva_tabla.append(info)

				for registro in registros_actuales:
					self.tabla.delete(registro)
				
				for (num,nombre,val,estado,est_pago) in nueva_tabla:
					self.tabla.insert('',END,text=num,values=(nombre,val,estado,est_pago))
			else:
				messagebox.showerror(message='No existe ningún pedido con el número de cédula del cliente ingresado',title='Cliente no encontrado')
						

	def actualizar_pedido(self):

		if len(self.entrada_id_pedido.get()) == 0:
			messagebox.showwarning(message='Debe introducir un ID de pedido',title='ID vacío')
		else:	
			pedido = Pedidos()
			id_pedido = int(self.entrada_id_pedido.get())
			
			if pedido.existe(id_pedido):
				cedula = pedido.retornar_cedula(id_pedido)
				ventana_eme = Tk()
				ventana_eme.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
				ventana_emergente = InterfazEmergente_productosPedidos(ventana_eme,cedula,id_pedido)
				ventana_emergente.pedido_nuevo = False
				ventana_emergente.mostrar_productos_pedido()
				ventana_eme.mainloop()
			else:
				messagebox.showerror(message='Pedido no registrado en la base de datos',title='ID no registrado')
					

	def volver_inicio(self):
		self.ventana.destroy()
		ventana = Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('420x275')
		aplicacion = ia.Inicio(ventana,self.inicio)
		ventana.mainloop()

