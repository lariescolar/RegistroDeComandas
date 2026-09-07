from abc import ABC, abstractmethod


class Tela(ABC):
    """
    Classe base para todas as telas do sistema.
    """

    @abstractmethod
    def exibir(self) -> None:
        """
        Exibe a tela para o usuário.
        """
        pass
