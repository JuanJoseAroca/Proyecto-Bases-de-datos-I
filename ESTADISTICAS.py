from Modelo import DatosEstadisticas as de 

class Estadisticas():
	def __init__(self):
		pass

	def valor_compras(self):
		return de.valor_compras()

	def valor_ventas_pagadas(self):
		return de.valor_ventas_pagadas()

	def valor_ventas_sin_pagar(self):
		return de.valor_ventas_sin_pagar()

	def cantidad_clientes(self):
		return de.cantidad_clientes()

	def promedio_compra_cliente(self):
		return de.promedio_compra_cliente()

	def promedio_pedidos_clientes(self):
		return de.promedio_pedidos_cliente()

	def producto_mas_demandado(self):
		return de.producto_mas_demandado()

	def numero_pedidos(self):
		return de.numero_pedidos()									