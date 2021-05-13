from Modelo import AccesoDelUsuario as adu

class Usuarios():
	def __init__(self):
		pass

	def acceder(self,usuario,contrasena):
		if adu.acceso_usuario(usuario,contrasena) != False:
			return True
		else:
			return False

	def cambiar_contrasena(self,usuario,contrasena_actual,nueva_constrasena):
		if self.acceder(usuario,contrasena_actual):
			if len(nueva_constrasena) >= 8:
				adu.cambio_contrasena(usuario,nueva_constrasena)
				return 'La contraseña fue exitosamente modificada'
			else:
				return 'Error, la contraseña debe tener al menos 8 caracteres'
		else:
			return 'Error en la validación de los datos'	


