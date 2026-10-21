from interface.tela import Tela
from modelos.mesa import Mesa
from lanchonete import Lanchonete
from excecoes.lanchonete_error import (
    MesaJaBloqueadaError,
    MesaJaDesbloqueadaError,
)


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

        status = "bloqueada" if mesa.bloqueada else "desbloqueada"
        ocupacao = "ocupada" if mesa.ocupada else "livre"
        print(f"A mesa {mesa.numero} está {status} e {ocupacao}.")

        if mesa.bloqueada:
            print("Situação: não pode receber novas comandas enquanto estiver bloqueada.")
        elif mesa.ocupada:
            print("Situação: não pode receber nova comanda, pois já possui uma em andamento.")
        else:
            print("Situação: disponível para abertura de comanda.")

    def bloquear_mesa(self) -> None:
        numero = _ler_int("Número da mesa: ")
        mesa = self.__lanchonete.localizar_mesa(numero)

        if mesa is None:
            print("Mesa não encontrada.")
            return

        try:
            self.__lanchonete.bloquear_mesa(mesa)
            print("Mesa bloqueada com sucesso.")
        except MesaJaBloqueadaError as exc:
            print(exc)

    def desbloquear_mesa(self) -> None:
        numero = _ler_int("Número da mesa: ")
        mesa = self.__lanchonete.localizar_mesa(numero)

        if mesa is None:
            print("Mesa não encontrada.")
            return

        try:
            self.__lanchonete.desbloquear_mesa(mesa)
            print("Mesa desbloqueada com sucesso.")
        except MesaJaDesbloqueadaError as exc:
            print(exc)
