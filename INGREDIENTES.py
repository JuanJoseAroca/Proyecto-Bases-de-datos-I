from Modelo import AdicionarDatos as add
from Modelo import BuscarTablas as bt
from Modelo import BuscarDatosObjeto as bdo
from Modelo import ObtenerDatoParticular as odp
from Modelo import ActualizarDatos as acd


class Ingredientes():
	def __init__(self):
		pass

	def obtener_tabla(self):
		return bt.obtener_tabla_ingredientes()

	def actualizar_disponibilidad(self,id_ingrediente,disponibilidad):
		acd.actualizar_disponibilidad_ingrediente(id_ingrediente,disponibilidad)

	def registrar(self,info):
		add.adicionar_ingrediente(info)			