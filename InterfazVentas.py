from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PEDIDOS import *
from PRODUCTOS import *
from CLIENTES import *
from InterfazCliente import *
from InterfazEmergenteProductosPedido import *
import InicioAdmin as ia
from InterfazEmergenteFactura import *


#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

class InterfazVenta():
	def __init__(self,ventana,tipo_inicio):
		self.inicio = tipo_inicio
		self.ventana = ventana
		self.ventana.title("P&C_DataBase - Ventas")
		self.ventana.configure(bg = DARKRED)
		self.marco1=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco1.grid(row=0,column=0,columnspan=4)

		#Lista de clientes
		c = Clientes()
		self.clientes = c.listar_clientes()
		self.cedulas = c.listar_cedulas()

		#Lista de estados del pago
		estados_pago = [
		'Pendiente',
		'Pagado']

		#Selección menú desplegable clientes
		self.variable_pago = StringVar(self.marco1)
		self.variable_pago.set(estados_pago[0])

		#Añadir pedido
		etiqueta_nombre = Label(self.marco1,text="Cambiar estado de pago de un pedido o ver factura del mismo",bg=DARKSALMON).grid(row=0,column=0)

		#Entrada de la venta a actualizar
		etiqueta_nombre = Label(self.marco1,text="Número de venta",bg=DARKSALMON).grid(row=1,column=0)
		self.entrada_venta = Entry(self.marco1)
		self.entrada_venta.grid(row=1,column=1)
		self.entrada_venta.focus()

		#Botón 1 (Actualizar estado de pago del  pedido)
		self.boton1 = ttk.Button(self.marco1,text="Actualizar estado de pago",command=self.modificar_estado_venta).grid(row=4, column=0,columnspan=1,sticky=W+E)

		#Botón 2 (Visualizar la factura de la venta)
		self.boton2 = ttk.Button(self.marco1,text="Ver factura",command=self.ver_factura,).grid(row=4, column=1,columnspan=1,sticky=W+E) 

		#Botón Inicio       
		self.boton5 = ttk.Button(ventana,text="Inicio",command=self.volver_inicio)
		self.boton5.place(x=0,y=0,width=100,height=30)

		#Menú desplegable (Clientes)
		etiqueta_menu1 = Label(self.marco1,text="Seleccionar estado de pago",bg=DARKSALMON).grid(row=3,column=0)
		self.opcion_clientes = OptionMenu(self.marco1,self.variable_pago,*estados_pago)
		self.opcion_clientes.grid(row=3,column=1,columnspan=2)


		#Mensaje
		self.mensaje=Label(text='',bg=DARKRED,fg='white')
		self.mensaje.place(x=100,y=100)

		#Tabla
		self.tabla=ttk.Treeview(self.ventana,columns=('#1','#2','#3','#4'))
		self.tabla.grid(row=8,column=0,columnspan=5)
		self.tabla.heading('#0',text='Número de venta')
		self.tabla.heading('#1',text='Numero pedido')
		self.tabla.heading('#2',text='Nombre cliente')
		self.tabla.heading('#3',text='Valor')
		self.tabla.heading('#4',text='Estado del pago')

		self.mostrar_datos()


	def mostrar_datos(self):
		ventas = Ventas()
		datos = ventas.obtener_tabla()
		registros_actuales = self.tabla.get_children()
		nueva_tabla = []

		for dato in datos:
			indice = self.cedulas.index(dato[2])
			info = (dato[0], dato[1], self.clientes[indice], '$' + str(dato[3]), dato[4])
			nueva_tabla.append(info)

		for registro in registros_actuales:
			self.tabla.delete(registro)

		for (id_venta,num_pedido,nombre,valor,estado) in nueva_tabla:
			self.tabla.insert('',END,text=id_venta,values=(num_pedido,nombre,valor,estado))

	def modificar_estado_venta(self):
		if len(self.entrada_venta.get()) > 0:
			nuevo_estado = self.variable_pago.get()
			id_venta = int(self.entrada_venta.get())
			venta = Ventas()
			if venta.existe(id_venta) == False:
				messagebox.showerror(message='Debe ingresar un ID de venta existente en la tabla', title='ID de venta no registrado')
			else:
				venta.actualizar_estado(id_venta,nuevo_estado)
			
			self.mostrar_datos()
		else:
			messagebox.showwarning(message='Debe ingresar un ID de venta', title='ID de venta vacío')	

	def buscar_pedidos(self):
		cedula = int(self.entrada_cedula_cliente.get())
		pedidos = Pedidos()
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

	def volver_inicio(self):
		self.ventana.destroy()
		ventana = Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('420x275')
		aplicacion = ia.Inicio(ventana,self.inicio)
		ventana.mainloop()

	def ver_factura(self):

		if len(self.entrada_venta.get()) > 0:
			pedido = Pedidos()
			num_pedido = int(self.entrada_venta.get())
			if pedido.existe(num_pedido):
				ventana=Tk()
				ventana.configure(bg = '#8B0000')
				ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
				aplicacion = InterfazEmergente_Factura(ventana,num_pedido)

				ventana.mainloop()
			else:
				messagebox.showerror(message='El ID de venta no está registrado en la base de datos', title='ID de venta no registrado')
		else:
			messagebox.showwarning(message='Debe ingresar un ID de venta', title='ID de venta vacío')			
								 					