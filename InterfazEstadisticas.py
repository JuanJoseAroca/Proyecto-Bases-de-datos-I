from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ESTADISTICAS import *
from PEDIDOS import *
from PRODUCTOS import *
from CLIENTES import *
import InicioAdmin as ia


#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

class InterfazEst():
	def __init__(self,ventana,tipo_inicio):
		self.inicio = tipo_inicio
		self.ventana = ventana
		self.ventana.title("P&C_DataBase - Estadísticas básicas")
		self.ventana.configure(bg = DARKRED)
		self.marco1=LabelFrame(self.ventana,bg=DARKSALMON)
		self.marco1.grid(row=3,column=0,columnspan=4)
		self.marco1.place(y=40)

		self.items_est = ['Compras (proveedores)',
					      'Ventas pagadas',
					      'Ventas sin pagar',
					      'N° clientes',
					      'Valor promedio de compra por cliente',
					      'Promedio pedidos por cliente',
					      'Producto más demandado'
		]

		#Tabla
		self.tabla=ttk.Treeview(self.marco1,columns=('#1'))
		self.tabla.grid(row=8,column=0,columnspan=1)
		self.tabla.heading('#0',text='Item')
		self.tabla.heading('#1',text='Estadística')
		
		self.tabla.column('#0',width=250)
		self.tabla.column('#1',width=200)

		self.boton3 = ttk.Button(ventana,text="Inicio",command=self.volver_inicio)
		self.boton3.place(x=0,y=0,width=70,height=30)

		self.mostrar_datos()

	def mostrar_datos(self):
		est = Estadisticas()

		if est.numero_pedidos() > 0:

			valores_est = []
			valores_est.append('$' + str(est.valor_compras()))
			valores_est.append('$' + str(est.valor_ventas_pagadas()))
			valores_est.append('$' + str(est.valor_ventas_sin_pagar()))
			valores_est.append(est.cantidad_clientes())
			valores_est.append('$' + str(round(est.promedio_compra_cliente(),2)))
			valores_est.append(round(est.promedio_pedidos_clientes(),2))
			valores_est.append(est.producto_mas_demandado())	


			for item in range(len(self.items_est)):
				self.tabla.insert('',END,text=self.items_est[item],values=(valores_est[item],))
		else:
			for item in range(len(self.items_est)):
				self.tabla.insert('',END,text=self.items_est[item],values=('',))		

	def volver_inicio(self):
		self.ventana.destroy()
		ventana = Tk()
		ventana.configure(bg = DARKRED)
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('420x275')
		aplicacion = ia.Inicio(ventana,self.inicio)
		ventana.mainloop()	
