from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from InterfazCliente import *
from USUARIOS import *
import CambioContrasena as cc
import InicioAdmin as ia
from tkinter.font import Font, nametofont


#Colores de la ventana
DARKSALMON = '#E9967A'
DARKRED = '#8B0000'
MAROON = '#800000'
LIGTHSEAGREEN = '#20B2AA'

class Linkbutton(ttk.Button):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtener el nombre de la fuente por defecto.
        label_font = nametofont("TkDefaultFont").cget("family")
        self.font = Font(family=label_font, size=9)
        
        # Crear un estilo para el hipervínculo.
        style = ttk.Style()
        style.configure(
            "Link.TLabel", foreground="#357fde", font=self.font)
        
        # Aplicarlo a la clase actual.
        self.configure(style="Link.TLabel", cursor="hand2")
        
        # Configurar los eventos de entrada y salida del mouse.
        self.bind("<Enter>", self.on_mouse_enter)
        self.bind("<Leave>", self.on_mouse_leave)
    
    def on_mouse_enter(self, event):
        # Aplicar subrayado.
        self.font.configure(underline=True)
    
    def on_mouse_leave(self, event):
        # Remover subrayado.
        self.font.configure(underline=False)


class Login():
	def __init__(self,ventana):
		self.ventana=ventana
		self.ventana.title("P&C_DataBase - Acceso")
		usuarios = [
		'',
		'Administrador',
		'Propietario'
		]
		marco1=LabelFrame(self.ventana,bg=DARKRED,fg='white')
		marco1.grid(row=2,column=5,columnspan=5)
		marco1.place(x=55,y=193)
		

		self.variable = StringVar(ventana)
		self.variable.set(usuarios[0])

		#Menú desplegable
		etiqueta_menu = Label(marco1,text="Tipo de usuario",bg=DARKRED,fg='white').grid(row=0,column=2)
		self.opcion = OptionMenu(marco1,self.variable,*usuarios)
		self.opcion.grid(row=0,column=3,columnspan=2)

		#Contraseña
		etiqueta_contraseña = Label(marco1,text="Contraseña",bg=DARKRED,fg='white').grid(row=1,column=2)
		self.contraseña = Entry(marco1, show='*')
		self.contraseña.grid(row=1,column=3)
		self.contraseña.focus()

		#Botón 1 (Validar contraseña)
		self.boton1 = ttk.Button(marco1,text="Validar",command=self.validar_contraseña)
		self.boton1.grid(row=4,column=2,columnspan=2,sticky=W+E)

		#Enlace de cambio de contraseña
		self.cambio_contrasena = Linkbutton(text= 'Cambiar contraseña', command=self.cambiar_contrasena)
		self.cambio_contrasena.place(x=110,y=280)


	def validar_contraseña(self):
		usuario = Usuarios()
		tipo_usuario = self.variable.get()
		contrasena = self.contraseña.get()

		if tipo_usuario == 'Administrador':
			if usuario.acceder(tipo_usuario,contrasena):
				self.abrir_inicio('Administrador')
			else:
				messagebox.showerror(message='Clave de administrador errónea',title='Verificar contraseña')
		elif tipo_usuario == 'Propietario':
			if usuario.acceder(tipo_usuario,contrasena):
				self.abrir_inicio('Propietario')
			else:
				messagebox.showerror(message='Clave de propietario errónea',title='Verificar contraseña')
		else:
			if self.variable.get() == '':
				messagebox.showerror(message='Por favor introduzca un tipo de usuario válido',title='Error de usuario')

	def abrir_inicio(self,usuario):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = '#8B0000')
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('420x275')
		aplicacion = ia.Inicio(ventana,usuario)
		ventana.mainloop()

	def cambiar_contrasena(self):
		self.ventana.destroy()
		ventana=Tk()
		ventana.configure(bg = '#8B0000')
		ventana.iconbitmap('C:\\Users\\home\\Desktop\\Semestre VI\\Bases de datos\\Proyecto\\Icono.ico')
		ventana.geometry('325x320')
		logo = PhotoImage(file="Logo.png")
		fondo = Label(ventana,image=logo).place(x=0,y=0)

		aplicacion = cc.MenuCambioCon(ventana)

		ventana.mainloop()	