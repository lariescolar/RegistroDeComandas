from interface.menu import Menu
from interface.telas.tela_atendimentos import TelaAtendimentos
from lanchonete import Lanchonete


class MenuAtendimentos(Menu):
    """Menu responsável pelas operações relacionadas aos atendimentos."""

    def __init__(self, lanchonete: Lanchonete) -> None:
        self.__tela = TelaAtendimentos(lanchonete)

    def executar(self) -> None:
        while True:
            print("\n===== Menu de Atendimentos =====")
            print("1 - Abrir atendimento")
            print("2 - Consultar atendimento")
            print("3 - Registrar pedido")
            print("4 - Registrar pagamento")
            print("5 - Encerrar atendimento")
            print("6 - Consultar histórico")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.__tela.abrir_atendimento()
            elif opcao == "2":
                self.__tela.consultar_atendimento()
            elif opcao == "3":
                self.__tela.registrar_pedido()
            elif opcao == "4":
                self.__tela.registrar_pagamento()
            elif opcao == "5":
                self.__tela.encerrar_atendimento()
            elif opcao == "6":
                self.__tela.consultar_historico()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
