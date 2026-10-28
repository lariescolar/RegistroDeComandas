from aplicacao import Aplicacao
from interface.menus.menu_principal import MenuPrincipal


def main() -> None:
    """Inicia a aplicação da lanchonete."""
    with Aplicacao() as aplicacao:
        menu = MenuPrincipal(aplicacao)
        menu.executar()


if __name__ == "__main__":
    main()
