from interface.tela import Tela
from modelos.produto import Produto, Suco, Sanduiche
from servicos.produto_service import ProdutoService
from excecoes.lanchonete_error import ProdutoNaoEncontradoError


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

    def __init__(self, produto_service: ProdutoService) -> None:
        self.__produto_service = produto_service

    def exibir(self) -> None:
        self.listar_produtos()

    def cadastrar_produto(self) -> None:
        codigo = _ler_int("Código do produto: ")

        try:
            self.__produto_service.localizar_produto(codigo)
            print("Esse produto já foi cadastrado.")
            return
        except ProdutoNaoEncontradoError:
            pass

        nome = input("Nome do produto: ").strip()
        preco = _ler_float("Preço do produto: ")
        tipo = input("Tipo (1 - Suco | 2 - Sanduíche): ").strip()

        disponivel_resposta = input("Produto disponível? (s/n): ").strip().lower()
        disponivel = disponivel_resposta in {"s", "sim", "y", "yes"}

        if tipo == "1":
            produto: Produto = Suco(codigo, nome, preco, disponivel)
        elif tipo == "2":
            produto = Sanduiche(codigo, nome, preco, disponivel)
        else:
            print("Tipo de produto inválido.")
            return

        self.__produto_service.cadastrar_produto(produto)
        print("Produto cadastrado com sucesso.")

    def listar_produtos(self) -> None:
        produtos = self.__produto_service.listar_produtos()

        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        print("\n--- Produtos ---")
        for produto in produtos:
            print(produto)

    def consultar_produto(self) -> None:
        codigo = _ler_int("Código do produto: ")

        try:
            produto = self.__produto_service.localizar_produto(codigo)
        except ProdutoNaoEncontradoError as exc:
            print(exc)
            return

        print(produto)
