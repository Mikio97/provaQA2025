# test_seguranca_pedidos.py

# Importa a função e a simulação de banco de dados do arquivo de referência
from sistema_pedidos import buscar_detalhes_pedido, DB_PEDIDOS 

def test_expor_falha_de_controle_de_acesso_idor():
    """
    Testa a falha de segurança IDOR (Insecure Direct Object Reference).
    Simula o Usuário 2 (atacante) tentando acessar o Pedido 101 (do Usuário 1).
    
    Atenção: Este teste FOI PROJETADO PARA FALHAR no código vulnerável.
    Ele passará apenas quando a função for corrigida para bloquear o acesso.
    """
    # Cenário de teste
    ID_PEDIDO_ALVO = 101  # Pedido que pertence ao Usuário 1
    ID_USUARIO_ATACANTE = 2 # Usuário logado tentando acessar um pedido que não é seu
    
    # 1. Executa a função vulnerável
    resultado_obtido = buscar_detalhes_pedido(ID_PEDIDO_ALVO, ID_USUARIO_ATACANTE)
    
    # 2. Define o resultado ESPERADO em um sistema SEGURO (Nenhum dado deve ser retornado)
    resultado_seguro_esperado = {}
    
    # 3. O 'assert' verifica se o sistema está SEGURO.
    # Como a função vulnerável retorna os detalhes do pedido, 
    # este 'assert' falhará (expondo a falha).
    assert resultado_obtido == resultado_seguro_esperado
    
    # Explicação da falha no código vulnerável:
    # A função retorna: {'item': 'Laptop', 'valor': 5000, 'id_usuario': 1}
    # O assert verifica: {'item': 'Laptop', 'valor': 5000, 'id_usuario': 1} == {}
    # Resultado: FALHA (Failure) - Vulnerabilidade exposta.

    