# portfolio-management-module

Repositorio para la postulación al cargo de Software Engineer en Fintual.

La clase Portfolio posee 3 métodos:
- get_total_value(): retorna el valor total de la cartera.
- target_values(): retorna los valores objetivo para cada stock según su asignación en allocated_stocks.
- rebalance(): retorna los ajustes necesarios para comprar o vender acciones según la asignación objetivo. No ejecuta las operaciones, solo las calcula. Si el valor es positivo, se deben comprar acciones; si es negativo, se deben vender; y si es 0, no se requieren ajustes para ese stock.

## Supuestos
- Se asume que todos los stocks definidos en allocated_stocks existen en self.stocks. Si no se posee alguno, se representa con stock.quantity = 0.
- Las asignaciones en allocated_stocks son válidas y suman el 100% de la cartera.

# Chat LLM
https://chatgpt.com/share/6ad7b111-3bdc-83e8-bbf3-3f7d75ffd666
