from aplicacao import Lanchonete
from interface.menus.menu_atendimentos import MenuAtendimentos
from interface.menus.menu_mesas import MenuMesas
from interface.menus.menu_principal import MenuPrincipal
from interface.menus.menu_produtos import MenuProdutos
from interface.telas.tela_atendimentos import TelaAtendimentos
from interface.telas.tela_mesas import TelaMesas
from interface.telas.tela_produtos import TelaProdutos
from servicos.atendimento_service import AtendimentoService
from servicos.mesa_service import MesaService
from servicos.pagamento_service import PagamentoService
from servicos.pedido_service import PedidoService
from servicos.produto_service import ProdutoService


def main() -> None:
    """Inicia a aplicação da lanchonete."""
    lanchonete = Lanchonete()

    mesa_service = MesaService(lanchonete)
    produto_service = ProdutoService(lanchonete)
    atendimento_service = AtendimentoService(lanchonete)
    pedido_service = PedidoService()
    pagamento_service = PagamentoService()

    tela_mesas = TelaMesas(mesa_service)
    tela_produtos = TelaProdutos(produto_service)
    tela_atendimentos = TelaAtendimentos(
        mesa_service,
        produto_service,
        atendimento_service,
        pedido_service,
        pagamento_service,
    )

    menu_mesas = MenuMesas(tela_mesas)
    menu_produtos = MenuProdutos(tela_produtos)
    menu_atendimentos = MenuAtendimentos(tela_atendimentos)
    menu_principal = MenuPrincipal(menu_mesas, menu_produtos, menu_atendimentos)

    menu_principal.executar()


if __name__ == "__main__":
    main()
