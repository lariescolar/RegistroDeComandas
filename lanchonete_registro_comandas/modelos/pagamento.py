class Pagamento:
    """Representa um pagamento realizado pelo cliente."""

    def __init__(self, valor: float, id_pagamento: int | None = None) -> None:
        self.__id: int | None = id_pagamento
        self.__valor: float = valor

    @property
    def id(self) -> int | None:
        return self.__id

    @property
    def valor(self) -> float:
        return self.__valor

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "valor": self.__valor,
        }

    @classmethod
    def from_dict(cls, dados: dict) -> "Pagamento":
        return cls(
            valor=float(dados["valor"]),
            id_pagamento=dados.get("id"),
        )

    def __str__(self) -> str:
        return f"R$ {self.__valor:.2f}"