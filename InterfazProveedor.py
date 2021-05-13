from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PEDIDOS import *
from PRODUCTOS import *
from CLIENTES import *
from CARTERA import *
from PROVEEDORES import *
from INGREDIENTES import *
from InterfazCliente import *
from InterfazEmergenteProductosPedido import *
import InicioAdmin as ia


#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

class InterfazProveedor():
	def __init__(self,ventana,tipo_inicio):
		self.inicio = tipo_inicio
		self.ventana = ventana
		self.ventana.title("P&C_DataBase - Proveedores")
		self.ventana.configure(bg = DARKRED)
		self.marco1=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco1.grid(row=0,column=1,columnspan=2)
		self.marco2=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco2.grid(row=0,column=3,columnspan=2)


		#Entrada del provedor
		etiqueta_proveedor = Label(self.marco1,text="Nombre del proveedor",bg=DARKSALMON).grid(row=0,column=0,columnspan=2)
		self.entrada_prov = Entry(self.marco1)
		self.entrada_prov.grid(row=0,column=2)
		self.entrada_prov.focus()
		etiqueta_valor = Label(self.marco1,text="Valor a pagar  $",bg=DARKSALMON).grid(row=1,column=0,columnspan=2)
		self.entrada_valor = Entry(self.marco1)
		self.entrada_valor.grid(row=1,column=2)

		#Entrada id del proveedor
		etiqueta_id = Label(self.marco2,text="ID del proveedor",bg=DARKSALMON).grid(row=0,column=1,columnspan=1)
		self.entrada_id = Entry(self.marco2)
		self.entrada_id.grid(row=0,column=2)

		#Botón 1 (Añadir proveedor)
		self.boton1 = ttk.Button(self.marco1,text="Añadir",command=self.agregar_proveedor).grid(row=2,columnspan=3,sticky=W+E)

		#Botón 2 (Borrar proveedor)
		self.boton2 = ttk.Button(self.marco2,text="Borrar proveedor",command=self.borrar_proveedor).grid(row=2,columnspan=3,sticky=W+E)

		#Botón inicio
		self.boton3 = ttk.Button(ventana,text="Inicio",command=self.volver_inicio)
		self.boton3.place(x=0,y=0,width=70,height=30)

		#Mensaje
		self.mensaje=Label(text='',bg=DARKRED,fg='white')
		self.mensaje.place(x=100,y=100)

		#Tabla
		self.tabla=ttk.Treeview(self.ventana,columns=('#1','#2'))
		self.tabla.grid(row=8,column=0,columnspan=5)
		self.tabla.heading('#0',text='ID')
		self.tabla.heading('#1',text='Proveedor')
		self.tabla.heading('#2',text='Valor de la compra')


		self.mostrar_datos()


	def mostrar_datos(self):
		provedor = Proveedores()
		datos = provedor.obtener_tabla()
		registros_actuales = self.tabla.get_children()
		nueva_tabla = []

		for dato in datos:
			info = (dato[0], dato[1], dato[2])
			nueva_tabla.append(info)

		for registro in registros_actuales:
			self.tabla.delete(registro)

		for (id_proveedor,proveedor,valor) in nueva_tabla:
			self.tabla.insert('',END,text=id_proveedor,values=(proveedor,'$' + str(valor)))

	def agregar_proveedor(self):
		if (len(self.entrada_prov.get()) > 0) and (len(self.entrada_valor.get()) > 0):
			proveedor = Proveedores()
			nombre_prov = self.entrada_prov.get()
			valor = int(self.entrada_valor.get())
			info = (nombre_prov,valor)
			proveedor.registrar(info)

			self.mostrar_datos()
		else:
			messagebox.showwarning(message='Por favor verifique los datos ingresados', title='Datos no válidos')	

	def borrar_proveedor(self):
		if len(self.entrada_id.get()) > 0:
			prov = Proveedores()
			id_proveedor = int(self.entrada_id.get())

			if prov.existe(id_proveedor):
				borrado = registro = messagebox.askyesno(message='¿Está segur@ que desea borrar este proveedor?',title='Borrar proveedor')
				if borrado:
					prov.borrar(id_proveedor)
					self.mostrar_datos()
			else:
				messagebox.showerror(message='El ID del proveedor ingresado no coincide con los registros de la base de datos', title='Proveedor no registrado')			
		else:
			messagebox.showwarning(message='Para borrar un proveedor debe ingresar su ID', title='ID Vacío')	

				

	def volver_inicio(self):
		self.ventana.destroy()
		ventana = Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('420x275')
		aplicacion = ia.Inicio(ventana,self.inicio)
		ventana.mainloop()	


