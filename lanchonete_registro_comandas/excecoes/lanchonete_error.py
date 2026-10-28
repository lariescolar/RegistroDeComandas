class LanchoneteError(Exception):
    """Exceção base do sistema da lanchonete."""
    pass


class DadoInvalidoError(LanchoneteError):
    """Indica que um dado informado é inválido (vazio, negativo etc.)."""
    pass


class MesaOcupadaError(LanchoneteError):
    """Indica que a mesa já possui um atendimento em andamento."""
    pass


class MesaJaCadastradaError(LanchoneteError):
    """Indica que já existe uma mesa com o número informado."""
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


class ProdutoJaCadastradoError(LanchoneteError):
    """Indica que já existe um produto com o código informado."""
    pass


class ProdutoIndisponivelError(LanchoneteError):
    """Indica que o produto não está disponível para venda."""
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
