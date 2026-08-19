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


# Registro de Comandas

## Componentes
- Vitória Vale de Oliveira Da Silva  
- Lucas Barbosa de Lima  
- Larissa Beatriz Teixeira de Sousa  

## Tema do projeto
**Registro de Comandas**

## Descrição
O projeto consiste em um sistema para controle de comandas de uma lanchonete, permitindo o cadastro de mesas e produtos, a abertura de atendimentos, o registro de pedidos e pagamentos, além do acompanhamento do saldo e do encerramento da comanda.
