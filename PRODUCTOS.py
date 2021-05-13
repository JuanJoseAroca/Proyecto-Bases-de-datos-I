from Modelo import AdicionarDatos as add
from Modelo import BuscarTablas as bt
from Modelo import BuscarDatosObjeto as bdo
from Modelo import ObtenerDatoParticular as odp

# Obtener los datos con el modelo
class Productos():
	def __init__(self):
		pass

	def obtener_tabla(self):
		return bt.obtener_tabla_productos()

	def registrar(self,info_producto):
		add.adicionar_producto(info_producto)

	def buscar(self,id_producto):
		return bdo.obtener_info_producto(id_producto)

	def nombre_producto(self,id_producto):
		return odp.obtener_nombre_producto(id_producto)

	def existe(self,nombre_producto):
		if bdo.obtener_info_producto_por_nombre(nombre_producto) != False:
			return True
		else:
			return False

	def listar_productos(self):
		productos = odp.listar_nombres_productos()
		return productos

	def listar_ids(self):
		ids = odp.listar_id_productos()
		return ids

	def listar_precios(self):
		precios = odp.listar_precios_productos()
		return precios





		
		