from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from CLIENTES import *
from InterfazProducto import *
from InicioAdmin import *

#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'

# Interfaz de usuario
class InterfazCliente:
    def __init__(self,ventana,tipo_inicio):
        self.ventana=ventana
        self.inicio = tipo_inicio
        self.ventana.configure(bg = DARKRED)
        self.ventana.title("P&C_DataBase - Clientes")
        marco1=LabelFrame(self.ventana,bg=DARKSALMON)
        marco1.grid(row=0,column=0,columnspan=2)
        marco2=LabelFrame(self.ventana,bg=DARKSALMON)
        marco2.grid(row=0,column=2,columnspan=2)
        #Nombre
        etiqueta_nombre = Label(marco1,text="Nombre(s)",bg=DARKSALMON).grid(row=0,column=0)
        self.entrada_nombre = Entry(marco1)
        self.entrada_nombre.grid(row=0,column=1)
        self.entrada_nombre.focus()

        #Apellidos
        etiqueta_apellidos = Label(marco1,text="Apellidos(s)",bg=DARKSALMON).grid(row=1,column=0)
        self.entrada_apellidos = Entry(marco1)
        self.entrada_apellidos.grid(row=1,column=1)

        #Cedula
        etiqueta_cedula = Label(marco1,text="Cédula",bg=DARKSALMON).grid(row=2,column=0)
        self.entrada_cedula = Entry(marco1)
        self.entrada_cedula.grid(row=2,column=1)

        etiqueta_telefono = Label(marco1,text="Celular/Telefono fijo",bg=DARKSALMON).grid(row=3,column=0)
        self.entrada_telefono = Entry(marco1)
        self.entrada_telefono.grid(row=3,column=1)

        #Busqueda de cliente
        etiqueta_buscar_cliente = Label(marco2,text="Cédula cliente",bg=DARKSALMON).grid(row=1,column=0)
        self.entrada_cedula_cliente = Entry(marco2)
        self.entrada_cedula_cliente.grid(row=1,column=1)
        
        #Botón 1 (Añadir cliente)
        self.boton1 = ttk.Button(marco1,text="Añadir cliente",command=self.ingresar_dato).grid(row=4,columnspan=2,sticky=W+E)

        #Botón 2 (Buscar cliente)
        self.boton2 = ttk.Button(marco2,text="Buscar cliente",command=self.buscar_cliente).grid(row=2,columnspan=2,sticky=W+E)

        #Botón 3 (Mostrar clientes)
        self.boton3 = ttk.Button(marco2,text="Mostrar todos los clientes",command=self.mostrar_datos).grid(row=3,columnspan=2,sticky=W+E)
 		
 		#Botón Inicio       
        self.boton4 = ttk.Button(ventana,text="Inicio",command=self.volver_inicio)
        self.boton4.place(x=0,y=0,width=75,height=30)
      
        #Tabla
        self.tabla=ttk.Treeview(self.ventana,columns=('#1','#2','#3','#4'))
        self.tabla.grid(row=6,column=0,columnspan=4)
        self.tabla.heading('#0',text='Cédula de ciudadanía')
        self.tabla.heading('#1',text='Nombre(s)')
        self.tabla.heading('#2',text='Apellido(s)')
        self.tabla.heading('#3',text='Número de pedidos')
        self.tabla.heading('#4',text='Número de contacto')  
        

    def mostrar_datos(self):
        clientes = Clientes()
        nueva_tabla = clientes.obtener_tabla()
        registros_actuales = self.tabla.get_children()
        
        for registro in registros_actuales:
            self.tabla.delete(registro)

        for  (cedula, nombres, apellidos, num_pedidos, telefono) in nueva_tabla:
            self.tabla.insert('',END,text=cedula,values=(nombres,apellidos,num_pedidos,telefono))    
    
    def ingresar_dato(self):
    	if len(self.entrada_cedula.get()) > 0 and len(self.entrada_nombre.get()) > 0 and len(self.entrada_apellidos.get()) > 0:
            cliente = Clientes()
            if (cliente.existe(self.entrada_cedula.get())):
                messagebox.showerror(message='La cédula ingresada coincide con un registro en la base de datos',title='Cédula anteriormente registrada')
            else:
                info = (int(self.entrada_cedula.get()), self.entrada_nombre.get(), self.entrada_apellidos.get(), 0, self.entrada_telefono.get())
                cliente.registrar(info)
    	else:
    		messagebox.showerror(message='Por favor verifique los datos ingresados',title='Datos no válidos')	

    def buscar_cliente(self):
    	cedula = self.entrada_cedula_cliente.get()
    	cliente = Clientes()
    	if cliente.existe(cedula) == True:
    		registros_actuales = self.tabla.get_children()
    		info = cliente.buscar(cedula)
    		
    		for registro in registros_actuales:
    			self.tabla.delete(registro)
    		
    		self.tabla.insert('',END,text=info[0],values=(info[1],info[2],info[3],info[4]))
    	else:
    		messagebox.showwarning(message='La cédula ingresada no coincide con ningún registro en la base de datos',title='Verificar cédula')

    def volver_inicio(self):
        self.ventana.destroy()
        ventana = Tk()
        ventana.configure(bg = DARKRED)
        ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
        ventana.geometry('420x275')
        aplicacion = Inicio(ventana,self.inicio)
        ventana.mainloop()

