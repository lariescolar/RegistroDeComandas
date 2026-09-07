from interface.menu import Menu


class MenuPrincipal(Menu):
    """Menu principal do sistema."""

    def __init__(self, menu_mesas: Menu, menu_produtos: Menu, menu_atendimentos: Menu) -> None:
        self.__menu_mesas = menu_mesas
        self.__menu_produtos = menu_produtos
        self.__menu_atendimentos = menu_atendimentos

    def executar(self) -> None:
        while True:
            print("\n===== Sabor da Orla =====")
            print("1 - Mesas")
            print("2 - Produtos")
            print("3 - Atendimentos")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.__menu_mesas.executar()
            elif opcao == "2":
                self.__menu_produtos.executar()
            elif opcao == "3":
                self.__menu_atendimentos.executar()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
