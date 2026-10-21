class LanchoneteError(Exception):
    """Exceção base do sistema da lanchonete."""
    pass


class MesaOcupadaError(LanchoneteError):
    """Indica que a mesa já possui um atendimento em andamento."""
    pass


class MesaBloqueadaError(LanchoneteError):
    """Indica que a mesa está bloqueada."""
    pass


class MesaJaBloqueadaError(LanchoneteError):
    """Indica que a mesa já está bloqueada."""
    pass


class MesaJaDesbloqueadaError(LanchoneteError):
    """Indica que a mesa já está desbloqueada."""
    pass


class AtendimentoEncerradoError(LanchoneteError):
    """Indica que o atendimento já foi encerrado."""
    pass


class AtendimentoNaoEncontradoError(LanchoneteError):
    """Indica que o atendimento solicitado não foi encontrado."""
    pass


class ProdutoNaoEncontradoError(LanchoneteError):
    """Indica que o produto solicitado não foi encontrado."""
    pass


class QuantidadeInvalidaError(LanchoneteError):
    """Indica que a quantidade informada é inválida."""
    pass


class PagamentoInvalidoError(LanchoneteError):
    """Indica que o pagamento informado é inválido."""
    pass


class AtendimentoNaoQuitadoError(LanchoneteError):
    """Indica que o atendimento ainda possui saldo pendente."""
    pass


class PersistenciaError(LanchoneteError):
    """Exceção base para erros na camada de persistência."""
    pass


class ArquivoCorrompidoError(PersistenciaError):
    """Indica que um arquivo JSON está corrompido ou com formato inválido."""
    pass


class RelacionamentoInvalidoError(PersistenciaError):
    """Indica que um ID referenciado no arquivo JSON não existe."""
    pass
