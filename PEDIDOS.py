from Modelo import AdicionarDatos as add
from Modelo import BuscarTablas as bt
from Modelo import BuscarDatosObjeto as bdo
from Modelo import ObtenerDatoParticular as odp
from Modelo import ActualizarDatos as acd

class Pedidos():
	def __init__(self):
		pass

	def obtener_tabla(self):
		return bt.obtener_tabla_pedidos()

	def registrar(self,info_pedido):
		add.adicionar_pedido(info_pedido)

	def buscar(self,cedula):
		return bdo.obtener_info_pedido(cedula)

	def seleccionar_id(self):
		return (odp.obtener_maximo_id_producto() + 1)

	def obtener_numero_pedido(self):
		maximo = odp.obtener_maximo_id_pedido()
		if maximo == None:
			return 1
		else:
			return maximo + 1

	def actualizar_valor(self,num_pedido,valor):
		acd.actualizar_valor_pedido(num_pedido,valor)

	def actualizar_estado(self,estado,num_pedido):
		acd.actualizar_estado_pedido(estado,num_pedido)

	def existe(self,num_pedido):
		if bdo.obtener_info_pedido_por_num_pedido(num_pedido) != []:
			return True
		else:
			return False	

	def existe_pedidos_cliente(self,cedula):
		if bdo.obtener_info_pedido(cedula) != []:
			return True
		else:
			return False

	def retornar_cedula(self,num_pedido):
		return odp.obtener_cedula_en_pedido(num_pedido)		

