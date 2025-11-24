# funcoes_validacao.py
def validar_senha(senha: str) -> bool:
    """
    Valida uma senha com as seguintes regras:
    - Pelo menos 8 caracteres.
    - Pelo menos um número.
    - Pelo menos uma letra maiúscula.
    """
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char.isupper() for char in senha):
        return False
    return True