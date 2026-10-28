from pathlib import Path

from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

# Importar o pacote "modelos" carrega todos os modelos ORM e registra seus
# mapeamentos em Base.metadata, o que é necessário antes de criar as tabelas.
from modelos import Base

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
PASTA_DADOS = RAIZ_PROJETO / "dados"
PASTA_DADOS.mkdir(exist_ok=True)

CAMINHO_BANCO = PASTA_DADOS / "lanchonete.db"

engine = create_engine(f"sqlite:///{CAMINHO_BANCO.as_posix()}")


@event.listens_for(engine, "connect")
def _ativar_chaves_estrangeiras(conexao, registro) -> None:
    """O SQLite não valida chaves estrangeiras por padrão; ativamos aqui."""
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def criar_tabelas() -> None:
    """Cria as tabelas que ainda não existem no banco."""
    Base.metadata.create_all(engine)


def criar_sessao() -> Session:
    """Cria uma nova sessão associada ao banco configurado."""
    return Session(engine)
