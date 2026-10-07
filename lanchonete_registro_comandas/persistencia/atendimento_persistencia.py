from typing import List
from modelos.atendimento import Atendimento
from modelos.mesa import Mesa
from modelos.pedido import Pedido
from modelos.pagamento import Pagamento
from persistencia.base_persistencia import BasePersistencia
from excecoes.lanchonete_error import RelacionamentoInvalidoError


class AtendimentoPersistencia(BasePersistencia):
    """Gerencia a persistência de objetos Atendimento em formato JSON."""

    def __init__(self, caminho: str = "dados/atendimentos.json") -> None:
        super().__init__(caminho)

    def carregar_todos(
        self,
        mesas: List[Mesa],
        pedidos: List[Pedido],
        pagamentos: List[Pagamento]
    ) -> List[Atendimento]:
        dados = self.carregar()
        
        mapa_mesas = {m.numero: m for m in mesas}
        mapa_pedidos = {p.id: p for p in pedidos if p.id is not None}
        mapa_pagamentos = {pg.id: pg for pg in pagamentos if pg.id is not None}

        atendimentos: List[Atendimento] = []
        for item in dados:
            # Aceita 'numero_mesa' ou 'mesa_numero' para evitar chave divergente
            num_mesa = item.get("numero_mesa")
            if num_mesa is None:
                num_mesa = item.get("mesa_numero")

            if num_mesa not in mapa_mesas:
                raise RelacionamentoInvalidoError(
                    f"Mesa #{num_mesa} referenciada no Atendimento #{item.get('id')} não existe."
                )

            mesa_obj = mapa_mesas[num_mesa]

            pedidos_atendimento = []
            for ped_id in item.get("pedido_ids", []):
                if ped_id is None:
                    continue
                if ped_id not in mapa_pedidos:
                    raise RelacionamentoInvalidoError(
                        f"Pedido #{ped_id} referenciado no Atendimento #{item.get('id')} não existe."
                    )
                pedidos_atendimento.append(mapa_pedidos[ped_id])

            pagamentos_atendimento = []
            for pag_id in item.get("pagamento_ids", []):
                if pag_id is None:
                    continue
                if pag_id not in mapa_pagamentos:
                    raise RelacionamentoInvalidoError(
                        f"Pagamento #{pag_id} referenciado no Atendimento #{item.get('id')} não existe."
                    )
                pagamentos_atendimento.append(mapa_pagamentos[pag_id])

            atendimento = Atendimento.from_dict(
                item,
                mesa=mesa_obj,
                pedidos=pedidos_atendimento,
                pagamentos=pagamentos_atendimento
            )
            atendimentos.append(atendimento)

        return atendimentos

    def salvar_todos(self, atendimentos: List[Atendimento]) -> None:
        self.salvar([a.to_dict() for a in atendimentos])