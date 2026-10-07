import json
import os
from pathlib import Path
from typing import List, Dict, Any
from excecoes.lanchonete_error import ArquivoCorrompidoError, PersistenciaError


class BasePersistencia:
    """Classe base genérica para operações I/O com arquivos JSON."""

    def __init__(self, caminho_arquivo: str) -> None:
        # Resolve o caminho absoluto relativo à raiz do projeto ('lanchonete_registro_comandas')
        raiz_projeto = Path(__file__).resolve().parent.parent
        self._caminho: str = str(raiz_projeto / caminho_arquivo)
        self._garantir_arquivo()

    def _garantir_arquivo(self) -> None:
        """Cria o diretório e o arquivo JSON vazio caso não existam."""
        diretorio = os.path.dirname(self._caminho)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio, exist_ok=True)
        if not os.path.exists(self._caminho):
            self.salvar([])

    def carregar(self) -> List[Dict[str, Any]]:
        """Lê os dados brutos em formato JSON."""
        try:
            with open(self._caminho, "r", encoding="utf-8") as f:
                conteudo = f.read().strip()
                if not conteudo:
                    return []
                return json.loads(conteudo)
        except json.JSONDecodeError as e:
            raise ArquivoCorrompidoError(f"Arquivo corrompido: '{self._caminho}'") from e
        except OSError as e:
            raise PersistenciaError(f"Erro ao acessar arquivo '{self._caminho}': {e}") from e

    def salvar(self, dados: List[Dict[str, Any]]) -> None:
        """Escreve os dados estruturados no arquivo JSON."""
        try:
            with open(self._caminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
        except OSError as e:
            raise PersistenciaError(f"Erro ao salvar em '{self._caminho}': {e}") from e