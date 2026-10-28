"""Serviços relacionados às mesas."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from excecoes.lanchonete_error import DadoInvalidoError, MesaJaCadastradaError
from modelos.mesa import Mesa


class MesaService:
    """Coordena as operações relacionadas às mesas."""

    def __init__(self, sessao: Session) -> None:
        self.__sessao = sessao

    def cadastrar_mesa(self, numero: int) -> Mesa:
        """Cadastra uma mesa com o número informado."""
        if numero <= 0:
            raise DadoInvalidoError("O número da mesa deve ser maior que zero.")

        if self.localizar_mesa(numero) is not None:
            raise MesaJaCadastradaError("Essa mesa já foi cadastrada.")

        mesa = Mesa(numero=numero, bloqueada=False)

        try:
            self.__sessao.add(mesa)
            self.__sessao.commit()
        except Exception:
            self.__sessao.rollback()
            raise

        return mesa

    def localizar_mesa(self, numero: int) -> Mesa | None:
        """Localiza uma mesa pelo número (chave primária)."""
        return self.__sessao.get(Mesa, numero)

    def listar_mesas(self) -> list[Mesa]:
        """Retorna as mesas cadastradas, ordenadas pelo número."""
        comando = select(Mesa).order_by(Mesa.numero)
        return list(self.__sessao.scalars(comando).all())

    def bloquear_mesa(self, mesa: Mesa) -> None:
        """Bloqueia uma mesa cadastrada."""
        try:
            mesa.bloquear()
            self.__sessao.commit()
        except Exception:
            self.__sessao.rollback()
            raise

    def desbloquear_mesa(self, mesa: Mesa) -> None:
        """Desbloqueia uma mesa cadastrada."""
        try:
            mesa.desbloquear()
            self.__sessao.commit()
        except Exception:
            self.__sessao.rollback()
            raise
