from Modelo import AdicionarDatos as add
from Modelo import BuscarTablas as bt
from Modelo import BuscarDatosObjeto as bdo
from Modelo import ObtenerDatoParticular as odp
from Modelo import ActualizarDatos as acd


# Obtener los datos con el modelo
class Clientes():
	def __init__(self):
		pass

	def obtener_tabla(self):
		return bt.obtener_tabla_clientes()

	def registrar(self,info_cliente):
		add.adicionar_cliente(info_cliente)

	def buscar(self,cedula):
		return bdo.obtener_info_cliente(cedula)

	def nombre_cliente(self,cedula):
		return odp.obtener_nombre_cliente(cedula)

	def existe(self,cedula):
		if bdo.obtener_info_cliente(cedula) != False:
			return True
		else:
			return False

	def listar_clientes(self):
		return odp.listar_nombres_clientes()

	def listar_cedulas(self):
		return odp.listar_cedulas_clientes()

	def adicionar_compra(self,cedula):
		acd.adicionar_compra_cliente(cedula)

	def listar_telefonos(self):
		return odp.listar_telefonos_clientes()	

	def cedula_en_pedido(self,num_pedido):
		return odp.obtener_cedula_cliente_por_pedido(num_pedido)	
								



		
			

