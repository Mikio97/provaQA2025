# sistema_pedidos.py
# Simulando um banco de dados de pedidos
DB_PEDIDOS = {
    101: {"item": "Laptop", "valor": 5000, "id_usuario": 1},
    102: {"item": "Mouse", "valor": 150, "id_usuario": 2},
}

def buscar_detalhes_pedido(id_do_pedido: int, id_do_usuario_logado: int) -> dict:
    """
    Busca os detalhes de um pedido.
    VULNERABILIDADE: Não verifica se o pedido pertence ao usuário logado.
    """
    if id_do_pedido in DB_PEDIDOS:
        return DB_PEDIDOS[id_do_pedido]
    return {}



