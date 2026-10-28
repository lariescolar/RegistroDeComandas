from interface.tela import Tela
from modelos.mesa import Mesa
from aplicacao import Aplicacao
from formatacao import formatar_moeda
from excecoes.lanchonete_error import (
    AtendimentoNaoEncontradoError,
    LanchoneteError,
)


def _ler_int(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


class TelaMesas(Tela):
    """Tela responsável pelas operações relacionadas às mesas."""

    def __init__(self, aplicacao: Aplicacao) -> None:
        self.__aplicacao = aplicacao

    def exibir(self) -> None:
        self.listar_mesas()

    def cadastrar_mesa(self) -> None:
        numero = _ler_int("Número da mesa: ")

        try:
            self.__aplicacao.mesa_service.cadastrar_mesa(numero)
            print("Mesa cadastrada com sucesso.")
        except LanchoneteError as exc:
            print(exc)

    def listar_mesas(self) -> None:
        mesas = self.__aplicacao.mesa_service.listar_mesas()

        if not mesas:
            print("Nenhuma mesa cadastrada.")
            return

        print("\n--- Situação das mesas ---")
        for mesa in mesas:
            print(self._descrever_mesa(mesa))

    def _descrever_mesa(self, mesa: Mesa) -> str:
        """Monta a linha de situação da mesa.

        - Disponível: mesa livre e desbloqueada;
        - Ocupada: exibe total e valor já pago do atendimento atual;
        - Indisponível (bloqueada): mesa bloqueada e sem atendimento.
        """
        if mesa.ocupada:
            situacao = "Ocupada (bloqueada)" if mesa.bloqueada else "Ocupada"
            try:
                atendimento = (
                    self.__aplicacao.atendimento_service.localizar_atendimento(mesa)
                )
            except AtendimentoNaoEncontradoError:
                return f"Mesa {mesa.numero} - {situacao}"
            return (
                f"Mesa {mesa.numero} - {situacao} - "
                f"Total: {formatar_moeda(atendimento.total)} - "
                f"Pago: {formatar_moeda(atendimento.total_pago)}"
            )

        if mesa.bloqueada:
            return f"Mesa {mesa.numero} - Indisponível (bloqueada)"

        return f"Mesa {mesa.numero} - Disponível"

    def consultar_disponibilidade(self) -> None:
        numero = _ler_int("Número da mesa: ")
        mesa = self.__aplicacao.mesa_service.localizar_mesa(numero)

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
        mesa = self.__aplicacao.mesa_service.localizar_mesa(numero)

        if mesa is None:
            print("Mesa não encontrada.")
            return

        try:
            self.__aplicacao.mesa_service.bloquear_mesa(mesa)
            print("Mesa bloqueada com sucesso.")
        except LanchoneteError as exc:
            print(exc)

    def desbloquear_mesa(self) -> None:
        numero = _ler_int("Número da mesa: ")
        mesa = self.__aplicacao.mesa_service.localizar_mesa(numero)

        if mesa is None:
            print("Mesa não encontrada.")
            return

        try:
            self.__aplicacao.mesa_service.desbloquear_mesa(mesa)
            print("Mesa desbloqueada com sucesso.")
        except LanchoneteError as exc:
            print(exc)
