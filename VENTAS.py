from Modelo import AdicionarDatos as add
from Modelo import BuscarTablas as bt
from Modelo import BuscarDatosObjeto as bdo
from Modelo import ObtenerDatoParticular as odp
from Modelo import ActualizarDatos as acd

class Ventas():
	def __init__(self):
		pass

	def obtener_tabla(self):
		return bt.obtener_tabla_ventas()

	def registrar(self,info_venta):
		add.adicionar_venta(info_venta)

	def buscar(self,id_venta):
		return bdo.obtener_info_venta(id_venta)

	def actualizar_valor(self,num_pedido,valor):
		acd.actualizar_valor_venta(num_pedido,valor)

	def actualizar_estado(self,id_venta,estado):
		acd.actualizar_estado_venta(id_venta,estado)

	def obtener_estado(self,num_pedido):
		return odp.obtener_estado_venta(num_pedido)

	def existe(self,id_venta):
		if bdo.obtener_info_venta(id_venta) != False:
			return True
		else:
			return False
						


			