from Modelo import AdicionarDatos as add
from Modelo import BuscarTablas as bt
from Modelo import BuscarDatosObjeto as bdo
from Modelo import ObtenerDatoParticular as odp
from Modelo import ActualizarDatos as acd
from Modelo import BorrarDatos as bd

class Proveedores():
	def __init__(self):
		pass

	def registrar(self,info):
		add.adicionar_proveedor(info)

	def borrar(self,id_proveedor):
		bd.borrar_registro_proveedor(id_proveedor)

	def obtener_tabla(self):
		return bt.obtener_tabla_proveedores()

	def existe(self,id_proveedor):
		if bdo.obtener_info_proveedor(id_proveedor) != False:
			return True
		else:
			return False	

				