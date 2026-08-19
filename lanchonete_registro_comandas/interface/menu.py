from abc import ABC, abstractmethod


class Menu(ABC):
    """
    Classe base para todos os menus do sistema.
    """

    @abstractmethod
    def executar(self) -> None:
        """
        Executa o menu.
        """
        pass
