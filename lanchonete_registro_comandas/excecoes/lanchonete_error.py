class LanchoneteError(Exception):
    """Exceção base do sistema da lanchonete."""
    pass


class MesaOcupadaError(LanchoneteError):
    """Indica que a mesa já possui um atendimento em andamento."""
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
