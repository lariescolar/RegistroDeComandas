from interface.menu import Menu
from interface.menus.menu_mesas import MenuMesas
from interface.menus.menu_produtos import MenuProdutos
from interface.menus.menu_atendimentos import MenuAtendimentos
from aplicacao import Aplicacao


class MenuPrincipal(Menu):
    """Menu principal do sistema."""

    def __init__(self, aplicacao: Aplicacao) -> None:
        self.__aplicacao = aplicacao

    def executar(self) -> None:
        while True:
            print("\n===== Sabor da Orla =====")
            print("1 - Mesas")
            print("2 - Produtos")
            print("3 - Atendimentos")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                MenuMesas(self.__aplicacao).executar()
            elif opcao == "2":
                MenuProdutos(self.__aplicacao).executar()
            elif opcao == "3":
                MenuAtendimentos(self.__aplicacao).executar()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
