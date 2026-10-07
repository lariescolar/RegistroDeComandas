from interface.tela import Tela
from modelos.produto import Produto, Suco, Sanduiche
from lanchonete import Lanchonete


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

    def __init__(self, lanchonete: Lanchonete) -> None:
        self.__lanchonete = lanchonete

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
            produto: Produto = Suco(codigo, nome, preco, disponivel)
        elif tipo == "2":
            produto = Sanduiche(codigo, nome, preco, disponivel)
        else:
            print("Tipo de produto inválido.")
            return

        self.__lanchonete.cadastrar_produto(produto)
        print("Produto cadastrado com sucesso.")

    def listar_produtos(self) -> None:
        produtos = self.__lanchonete.produtos

        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        print("\n--- Produtos ---")
        for produto in produtos:
            print(produto)

    def consultar_produto(self) -> None:
        codigo = _ler_int("Código do produto: ")

        try:
            produto = self.__lanchonete.localizar_produto(codigo)
        except Exception as exc:
            print(exc)
            return

        print(produto)
