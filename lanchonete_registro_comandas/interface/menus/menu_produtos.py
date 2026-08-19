from interface.menu import Menu
from interface.telas.tela_produtos import TelaProdutos
from lanchonete import Lanchonete


class MenuProdutos(Menu):
    """Menu de produtos do sistema."""

    def __init__(self, lanchonete: Lanchonete) -> None:
        self.__tela = TelaProdutos(lanchonete)

    def executar(self) -> None:
        while True:
            print("\n===== Menu de Produtos =====")
            print("1 - Cadastrar produto")
            print("2 - Listar produtos")
            print("3 - Consultar produto")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.__tela.cadastrar_produto()
            elif opcao == "2":
                self.__tela.listar_produtos()
            elif opcao == "3":
                self.__tela.consultar_produto()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
