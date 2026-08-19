from interface.menu import Menu
from interface.telas.tela_mesas import TelaMesas
from lanchonete import Lanchonete


class MenuMesas(Menu):
    """Menu responsável pelas operações relacionadas às mesas."""

    def __init__(self, lanchonete: Lanchonete) -> None:
        self.__tela = TelaMesas(lanchonete)

    def executar(self) -> None:
        while True:
            print("\n===== Menu de Mesas =====")
            print("1 - Cadastrar mesa")
            print("2 - Listar mesas")
            print("3 - Consultar disponibilidade")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.__tela.cadastrar_mesa()
            elif opcao == "2":
                self.__tela.listar_mesas()
            elif opcao == "3":
                self.__tela.consultar_disponibilidade()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
