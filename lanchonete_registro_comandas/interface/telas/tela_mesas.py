from interface.tela import Tela
from modelos.mesa import Mesa
from lanchonete import Lanchonete


def _ler_int(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


class TelaMesas(Tela):
    """Tela responsável pelas operações relacionadas às mesas."""

    def __init__(self, lanchonete: Lanchonete) -> None:
        self.__lanchonete = lanchonete

    def exibir(self) -> None:
        self.listar_mesas()

    def cadastrar_mesa(self) -> None:
        numero = _ler_int("Número da mesa: ")

        if self.__lanchonete.localizar_mesa(numero) is not None:
            print("Essa mesa já foi cadastrada.")
            return

        self.__lanchonete.cadastrar_mesa(Mesa(numero))
        print("Mesa cadastrada com sucesso.")

    def listar_mesas(self) -> None:
        mesas = self.__lanchonete.mesas

        if not mesas:
            print("Nenhuma mesa cadastrada.")
            return

        print("\n--- Mesas ---")
        for mesa in mesas:
            print(mesa)

    def consultar_disponibilidade(self) -> None:
        numero = _ler_int("Número da mesa: ")
        mesa = self.__lanchonete.localizar_mesa(numero)

        if mesa is None:
            print("Mesa não encontrada.")
            return

        status = "ocupada" if mesa.ocupada else "disponível"
        print(f"A mesa {mesa.numero} está {status}.")
