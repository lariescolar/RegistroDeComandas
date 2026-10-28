from interface.tela import Tela
from modelos.produto import Suco, Sanduiche
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


class TelaProdutos(Tela):
    """Tela responsável pelas operações relacionadas aos produtos."""

    def __init__(self, aplicacao: Aplicacao) -> None:
        self.__aplicacao = aplicacao

    def exibir(self) -> None:
        self.listar_produtos()

    def cadastrar_produto(self) -> None:
        codigo = _ler_int("Código do produto: ")
        nome = input("Nome do produto: ").strip()
        preco = _ler_float("Preço do produto: ")
        tipo = input("Tipo (1 - Suco | 2 - Sanduíche): ").strip()

        disponivel_resposta = input("Produto disponível? (s/n): ").strip().lower()
        disponivel = disponivel_resposta in {"s", "sim", "y", "yes"}

        if tipo == "1":
            classe = Suco
        elif tipo == "2":
            classe = Sanduiche
        else:
            print("Tipo de produto inválido.")
            return

        try:
            self.__aplicacao.produto_service.cadastrar_produto(
                classe, codigo, nome, preco, disponivel
            )
            print("Produto cadastrado com sucesso.")
        except LanchoneteError as exc:
            print(exc)

    def listar_produtos(self) -> None:
        produtos = self.__aplicacao.produto_service.listar_produtos()

        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        print("\n--- Produtos ---")
        for produto in produtos:
            print(produto)

    def consultar_produto(self) -> None:
        codigo = _ler_int("Código do produto: ")

        try:
            produto = self.__aplicacao.produto_service.localizar_produto(codigo)
        except LanchoneteError as exc:
            print(exc)
            return

        print(produto)
