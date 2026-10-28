from interface.tela import Tela
from formatacao import formatar_moeda
from aplicacao import Aplicacao
from excecoes.lanchonete_error import LanchoneteError


def _ler_int(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def _ler_float(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")


class TelaAtendimentos(Tela):
    """Tela responsável pelas operações relacionadas aos atendimentos."""

    def __init__(self, aplicacao: Aplicacao) -> None:
        self.__aplicacao = aplicacao

    def exibir(self) -> None:
        self.consultar_historico()

    def exibir_totais_gerais(self) -> None:
        """Exibe o total geral dos atendimentos e dos pagamentos registrados."""
        servico = self.__aplicacao.atendimento_service
        print(f"Total dos atendimentos: {formatar_moeda(servico.total_geral_atendimentos())}")
        print(f"Total pago: {formatar_moeda(servico.total_geral_pagamentos())}")

    def _ler_mesa(self):
        numero = _ler_int("Número da mesa: ")
        mesa = self.__aplicacao.mesa_service.localizar_mesa(numero)
        if mesa is None:
            print("Mesa não encontrada.")
            return None
        return mesa

    def _ler_atendimento_aberto(self):
        """Lê a mesa e devolve o atendimento em aberto dela (ou None)."""
        mesa = self._ler_mesa()
        if mesa is None:
            return None

        try:
            return self.__aplicacao.atendimento_service.localizar_atendimento(mesa)
        except LanchoneteError as exc:
            print(exc)
            return None

    def abrir_atendimento(self) -> None:
        mesa = self._ler_mesa()
        if mesa is None:
            return

        try:
            self.__aplicacao.atendimento_service.abrir_atendimento(mesa)
            print(f"Atendimento aberto para a mesa {mesa.numero}.")
        except LanchoneteError as exc:
            print(exc)

    def consultar_atendimento(self) -> None:
        atendimento = self._ler_atendimento_aberto()
        if atendimento is None:
            return

        print("\n--- Atendimento ---")
        print(atendimento)

        if atendimento.pedidos:
            print("\nPedidos:")
            for pedido in atendimento.pedidos:
                print(f"- {pedido}")
        else:
            print("\nNenhum pedido registrado.")

        if atendimento.pagamentos:
            print("\nPagamentos:")
            for pagamento in atendimento.pagamentos:
                print(f"- {pagamento}")
        else:
            print("\nNenhum pagamento registrado.")

    def registrar_pedido(self) -> None:
        atendimento = self._ler_atendimento_aberto()
        if atendimento is None:
            return

        codigo = _ler_int("Código do produto: ")

        try:
            produto = self.__aplicacao.produto_service.localizar_produto(codigo)
        except LanchoneteError as exc:
            print(exc)
            return

        if not produto.disponivel:
            print("Esse produto está indisponível.")
            return

        quantidade = _ler_int("Quantidade: ")

        try:
            self.__aplicacao.pedido_service.registrar_pedido(
                atendimento, produto, quantidade
            )
            print("Pedido registrado com sucesso.")
        except LanchoneteError as exc:
            print(exc)

    def registrar_pagamento(self) -> None:
        atendimento = self._ler_atendimento_aberto()
        if atendimento is None:
            return

        valor = _ler_float("Valor do pagamento: ")

        try:
            self.__aplicacao.pagamento_service.registrar_pagamento(
                atendimento, valor
            )
            print("Pagamento registrado com sucesso.")
        except LanchoneteError as exc:
            print(exc)

    def encerrar_atendimento(self) -> None:
        atendimento = self._ler_atendimento_aberto()
        if atendimento is None:
            return

        try:
            self.__aplicacao.atendimento_service.encerrar_atendimento(atendimento)
            print("Atendimento encerrado com sucesso.")
        except LanchoneteError as exc:
            print(exc)

    def consultar_historico(self) -> None:
        atendimentos = self.__aplicacao.atendimento_service.consultar_historico()

        if not atendimentos:
            print("Nenhum atendimento registrado.")
            return

        print("\n--- Histórico de atendimentos ---")
        for atendimento in atendimentos:
            print(atendimento)
