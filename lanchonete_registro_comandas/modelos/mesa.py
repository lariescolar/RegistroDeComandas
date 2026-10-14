class Mesa:
    """Representa uma mesa da lanchonete."""

    def __init__(self, numero: int) -> None:
        self.__numero: int = numero
        self.__ocupada: bool = False
        self.__bloqueada: bool = False

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def ocupada(self) -> bool:
        return self.__ocupada
    
    @property
    def bloqueada (self) -> bool:
        return self.__bloqueada

    def ocupar(self) -> None:
        self.__ocupada = True

    def liberar(self) -> None:
        self.__ocupada = False

    def bloquear(self) -> None:
        self.__bloqueada = True

    def desbloquear(self) -> None:
        self.__bloqueada = False

    def to_dict(self) -> dict:
        return {
            "numero": self.__numero,
            "ocupada": self.__ocupada,
            "bloqueada": self.__bloqueada,
        }

    @classmethod
    def from_dict(cls, dados: dict) -> "Mesa":
        mesa = cls(numero=int(dados["numero"]))
        mesa.__ocupada = bool(dados.get("ocupada", False))
        mesa.__bloqueada = bool(dados.get("bloqueada", False))
        return mesa

    def __str__(self) -> str:
        status = "Indisponível" if self.__ocupada or self.__bloqueada else "Disponível"
        return f"Mesa {self.__numero} - {status}"
