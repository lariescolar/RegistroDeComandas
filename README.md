```mermaid
erDiagram
    MESA ||--o{ ATENDIMENTO : possui
    ATENDIMENTO ||--o{ PEDIDO : registra
    PRODUTO ||--o{ PEDIDO : compoe
    ATENDIMENTO ||--o{ PAGAMENTO : recebe

    MESA {
        int numero PK
        bool ocupada
    }

    ATENDIMENTO {
        int id_atendimento PK
        int numero_mesa FK
        bool encerrado
        float total
        float total_pago
        float saldo
    }

    PRODUTO {
        int codigo PK
        string nome
        float preco
        bool disponivel
    }

    PEDIDO {
        int id_pedido PK
        int id_atendimento FK
        int codigo_produto FK
        int quantidade
        float valor
    }

    PAGAMENTO {
        int id_pagamento PK
        int id_atendimento FK
        float valor
        datetime data
    }

```md
Este diagrama mostra a estrutura principal do sistema de registro de comandas. Uma mesa pode ter vários atendimentos ao longo do tempo, cada atendimento pode registrar vários pedidos e pagamentos, e cada pedido está vinculado a um produto específico.
