from lanchonete import Lanchonete
from interface.menus.menu_principal import MenuPrincipal


def main() -> None:
    """Inicia a aplicação da lanchonete."""
    lanchonete = Lanchonete()
    menu = MenuPrincipal(lanchonete)
    menu.executar()


if __name__ == "__main__":
    main()
