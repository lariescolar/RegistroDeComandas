class Pagamento:
    """Representa um pagamento realizado pelo cliente."""

    def __init__(self, valor: float) -> None:
        self.__valor: float = valor

    @property
    def valor(self) -> float:
        return self.__valor

    def __str__(self) -> str:
        return f"R$ {self.__valor:.2f}"
