


from funcoes_validacao import validar_senha 


def test_01_senha_valida_completa():
    senha_forte = "Exemplo123Forte"
    assert validar_senha(senha_forte) is True


def test_02_senha_curta():
    senha_curta = "Abc12"
    assert validar_senha(senha_curta) is False


def test_03_senha_sem_numero():
    senha_sem_num = "SenhaCompridaSemNumero"
    assert validar_senha(senha_sem_num) is False


def test_04_senha_sem_maiuscula():
    senha_sem_upper = "senhacom8digitos123"
    assert validar_senha(senha_sem_upper) is False