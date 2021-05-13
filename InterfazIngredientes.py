from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PEDIDOS import *
from PRODUCTOS import *
from CLIENTES import *
from CARTERA import *
from INGREDIENTES import *
from InterfazCliente import *
from InterfazEmergenteProductosPedido import *
import InicioAdmin as ia


#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

class InterfazIngrediente():
	def __init__(self,ventana,tipo_inicio):
		self.inicio = tipo_inicio
		self.ventana = ventana
		self.ventana.title("P&C_DataBase - Stock/ingredientes")
		self.ventana.configure(bg = DARKRED)
		self.marco1=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco1.grid(row=0,column=1,columnspan=2)
		self.marco2=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco2.grid(row=0,column=3,columnspan=2)
		self.marco1.place(x=85,y=10)



		self.disponibilidades = [
		'Disponible',
		'No disponible']

		#Entrada dato de ingrediente
		etiqueta_ingrediente = Label(self.marco1,text="Nombre del ingrediente",bg=DARKSALMON).grid(row=0,column=0,columnspan=2)
		self.entrada_nombre = Entry(self.marco1)
		self.entrada_nombre.grid(row=0,column=2)
		self.entrada_nombre.focus()


		#Actualizar disponibilidad
		etiqueta_id = Label(self.marco2,text="ID del ingrediente",bg=DARKSALMON).grid(row=0,column=0,columnspan=1)
		self.entrada_id = Entry(self.marco2)
		self.entrada_id.grid(row=0,column=1)
		self.entrada_id.focus()

		#Selección menú desplegable clientes
		self.variable_dispo = StringVar(self.marco2)
		self.variable_dispo.set(self.disponibilidades[0])


		#Botón 1 (Añadir ingrediente)
		self.boton1 = ttk.Button(self.marco1,text="Añadir",command=self.agregar_ingrediente).grid(row=1,columnspan=3,sticky=W+E)

		#Botón 2 (Actualizar disponibilidad)
		self.boton2 = ttk.Button(self.marco2,text="Actualizar disponibilidad",command=self.actualizar_disponibilidad).grid(row=2,columnspan=3,sticky=W+E)

		#Menú desplegable (Clientes)
		etiqueta_menu1 = Label(self.marco2,text="Seleccionar disponibilidad",bg=DARKSALMON).grid(row=1,column=0)
		self.opcion_dispo = OptionMenu(self.marco2,self.variable_dispo,*self.disponibilidades)
		self.opcion_dispo.grid(row=1,column=1,columnspan=2)

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
		self.tabla.heading('#1',text='Ingrediente')
		self.tabla.heading('#2',text='Disponibilidad')


		self.mostrar_datos()


	def mostrar_datos(self):
		ingrediente = Ingredientes()
		datos = ingrediente.obtener_tabla()
		registros_actuales = self.tabla.get_children()
		nueva_tabla = []

		for dato in datos:
			info = (dato[0], dato[1], dato[2])
			nueva_tabla.append(info)

		for registro in registros_actuales:
			self.tabla.delete(registro)

		for (id_ingrediente,ingrediente,disponibilidad) in nueva_tabla:
			self.tabla.insert('',END,text=id_ingrediente,values=(ingrediente,disponibilidad))
		
	def actualizar_disponibilidad(self):
		if len(self.entrada_id.get()) > 0:
			ingrediente = Ingredientes()
			id_ingrediente = int(self.entrada_id.get())
			disponibilidad = self.variable_dispo.get()
			ingrediente.actualizar_disponibilidad(id_ingrediente,disponibilidad)
			self.mostrar_datos()
		else:
			messagebox.showwarning(message='Debe ingresar el nombre ID algún ingrediente de la tabla',title='ID de ingrediente vacío')	
	

	def agregar_ingrediente(self):
		ingrediente = Ingredientes()
		nombre_ing = self.entrada_nombre.get()
		if len(nombre_ing) > 0:
			dispo = 'Disponible'
			info = (nombre_ing,dispo)
			ingrediente.registrar(info)
		else:
			messagebox.showwarning(message='Debe ingresar el nombre de algún ingrediente',title='Nombre de ingrediente vacío')	

		self.mostrar_datos()

	def volver_inicio(self):
		self.ventana.destroy()
		ventana = Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('420x275')
		aplicacion = ia.Inicio(ventana,self.inicio)
		ventana.mainloop()
					
