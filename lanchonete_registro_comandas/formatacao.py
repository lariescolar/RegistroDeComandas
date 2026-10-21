"""Funções auxiliares de formatação de valores."""


def formatar_moeda(valor: float) -> str:
    """Formata um valor no padrão brasileiro. Ex.: 1234.5 -> 'R$ 1.234,50'."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {texto}"
