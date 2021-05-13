from Modelo import AdicionarDatos as add
from Modelo import BuscarTablas as bt
from Modelo import BuscarDatosObjeto as bdo
from Modelo import ObtenerDatoParticular as odp

class Productos_pedidos():
	def __init__(self):
		pass

	def registrar(self,info):
		add.adicionar_producto_pedido(info)

	def obtener_producto_pedido(self,num_pedido):
		return bdo.obtener_info_producto_pedido(num_pedido)

			
		