from interface.tela import Tela
from modelos.pedido import Pedido
from modelos.pagamento import Pagamento
from lanchonete import Lanchonete
from excecoes.lanchonete_error import (
    AtendimentoNaoEncontradoError,
    AtendimentoNaoQuitadoError,
    MesaOcupadaError,
    PagamentoInvalidoError,
    ProdutoNaoEncontradoError,
    QuantidadeInvalidaError,
)


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

    def __init__(self, lanchonete: Lanchonete) -> None:
        self.__lanchonete = lanchonete

    def exibir(self) -> None:
        self.consultar_historico()

    def _ler_mesa(self):
        numero = _ler_int("Número da mesa: ")
        mesa = self.__lanchonete.localizar_mesa(numero)
        if mesa is None:
            print("Mesa não encontrada.")
            return None
        return mesa

    def abrir_atendimento(self) -> None:
        mesa = self._ler_mesa()
        if mesa is None:
            return

        try:
            self.__lanchonete.abrir_atendimento(mesa)
            print(f"Atendimento aberto para a mesa {mesa.numero}.")
        except MesaOcupadaError as exc:
            print(exc)

    def consultar_atendimento(self) -> None:
        mesa = self._ler_mesa()
        if mesa is None:
            return

        try:
            atendimento = self.__lanchonete.localizar_atendimento(mesa)
        except AtendimentoNaoEncontradoError as exc:
            print(exc)
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
        mesa = self._ler_mesa()
        if mesa is None:
            return

        try:
            atendimento = self.__lanchonete.localizar_atendimento(mesa)
        except AtendimentoNaoEncontradoError as exc:
            print(exc)
            return

        codigo = _ler_int("Código do produto: ")

        try:
            produto = self.__lanchonete.localizar_produto(codigo)
        except ProdutoNaoEncontradoError as exc:
            print(exc)
            return

        if not produto.disponivel:
            print("Esse produto está indisponível.")
            return

        quantidade = _ler_int("Quantidade: ")

        try:
            pedido = Pedido(produto, quantidade)
            self.__lanchonete.registrar_pedido(atendimento, pedido)
            print("Pedido registrado com sucesso.")
        except QuantidadeInvalidaError as exc:
            print(exc)

    def registrar_pagamento(self) -> None:
        mesa = self._ler_mesa()
        if mesa is None:
            return

        try:
            atendimento = self.__lanchonete.localizar_atendimento(mesa)
        except AtendimentoNaoEncontradoError as exc:
            print(exc)
            return

        valor = _ler_float("Valor do pagamento: ")

        try:
            pagamento = Pagamento(valor)
            self.__lanchonete.registrar_pagamento(atendimento, pagamento)
            print("Pagamento registrado com sucesso.")
        except PagamentoInvalidoError as exc:
            print(exc)

    def encerrar_atendimento(self) -> None:
        mesa = self._ler_mesa()
        if mesa is None:
            return

        try:
            atendimento = self.__lanchonete.localizar_atendimento(mesa)
        except AtendimentoNaoEncontradoError as exc:
            print(exc)
            return

        try:
            self.__lanchonete.encerrar_atendimento(atendimento)
            print("Atendimento encerrado com sucesso.")
        except AtendimentoNaoQuitadoError as exc:
            print(exc)

    def consultar_historico(self) -> None:
        atendimentos = self.__lanchonete.consultar_atendimentos()

        if not atendimentos:
            print("Nenhum atendimento registrado.")
            return

        print("\n--- Histórico de atendimentos ---")
        for atendimento in atendimentos:
            print(atendimento)
