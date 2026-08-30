# 🍔 Registro de Comandas — Sabor da Orla

Sistema orientado a objetos desenvolvido para a lanchonete **Sabor da Orla**, com o objetivo de substituir o controle manual de comandas de papel por um sistema informatizado.

---

## 👥 Equipe

- Vitória Vale de Oliveira Da Silva
- Lucas Barbosa de Lima
- Larissa Beatriz Teixeira de Sousa

---

## 📌 Sobre o projeto

O sistema permite controlar as comandas da lanchonete desde a abertura do atendimento até o seu encerramento.

Durante um atendimento, é possível registrar os produtos consumidos, acompanhar o valor total da comanda, realizar pagamentos parciais, consultar o valor já pago e verificar o saldo restante.

Após a quitação da conta, o atendimento pode ser encerrado e a mesa volta a ficar disponível. Os atendimentos encerrados permanecem registrados para consulta do histórico.

Os dados são mantidos **em memória durante a execução do programa**.

---

## ⚙️ Funcionalidades

### 🪑 Mesas
- Cadastrar mesas;
- Listar mesas;
- Consultar disponibilidade;
- Ocupar uma mesa ao abrir um atendimento;
- Liberar a mesa após o encerramento.

### 🍹 Produtos
- Cadastrar produtos;
- Listar produtos;
- Consultar produtos;
- Trabalhar com diferentes tipos de produtos utilizando herança e polimorfismo.

### 🧾 Atendimentos
- Abrir atendimento;
- Consultar uma comanda;
- Registrar pedidos;
- Consultar o consumo;
- Registrar pagamentos;
- Consultar pagamentos;
- Consultar o saldo;
- Encerrar atendimento;
- Consultar o histórico.

### 💳 Pagamentos
- Registrar pagamentos parciais;
- Consultar o total pago;
- Calcular o saldo restante;
- Impedir pagamentos superiores ao saldo da comanda.

---

## 🏗️ Estrutura do projeto

```
RegistroDeComandas/
│
├── main.py
├── lanchonete.py
│
├── modelos/
│   ├── __init__.py
│   ├── mesa.py
│   ├── atendimento.py
│   ├── produto.py
│   ├── pedido.py
│   └── pagamento.py
│
├── excecoes/
│   ├── __init__.py
│   ├── lanchonete_error.py
│   └── ...
│
└── interface/
    ├── __init__.py
    ├── menu.py
    ├── tela.py
    │
    ├── menus/
    │   ├── __init__.py
    │   ├── menu_principal.py
    │   ├── menu_mesas.py
    │   ├── menu_produtos.py
    │   └── menu_atendimentos.py
    │
    └── telas/
        ├── __init__.py
        ├── tela_mesas.py
        ├── tela_produtos.py
        └── tela_atendimentos.py
```

🧩 Modelos

O sistema possui os seguintes modelos principais:

Mesa
Atendimento
Produto
Pedido
Pagamento

A classe Produto é abstrata e utiliza herança e polimorfismo para representar diferentes tipos de produtos.

Os objetos se relacionam por meio de referências aos próprios objetos, mantendo a integração entre os modelos.

🔗 Relacionamentos

Os principais relacionamentos entre os objetos são:

Mesa 1 ───────── N Atendimento

Atendimento 1 ───────── N Pedido

Produto 1 ───────── N Pedido

Atendimento 1 ───────── N Pagamento

Uma mesa pode possuir vários atendimentos ao longo do tempo, porém apenas um atendimento pode estar aberto simultaneamente.

Um atendimento pode possuir vários pedidos e vários pagamentos.

Cada pedido está associado a um produto.

💰 Controle da comanda

O Atendimento calcula automaticamente as informações financeiras da comanda.

Total
= soma dos valores dos pedidos

Total pago
= soma dos valores dos pagamentos

Saldo
= Total - Total pago

Esses valores são calculados a partir dos objetos existentes e não são armazenados manualmente.

⚠️ Regras de negócio

Mesas
- Não é permitido abrir dois atendimentos simultaneamente para a mesma mesa.
- Uma mesa ocupada não pode receber um novo atendimento.

Atendimentos
- Não é permitido registrar pedidos em um atendimento encerrado.
- Não é permitido registrar pagamentos em um atendimento encerrado.
- Não é permitido encerrar um atendimento com saldo pendente.
- Após o encerramento, a mesa volta a ficar disponível.
- O atendimento encerrado permanece no histórico.

Pedidos
- A quantidade deve ser maior que zero.
- O pedido deve estar associado a um produto existente.

Pagamentos
- O valor do pagamento deve ser maior que zero.
- Não é permitido realizar pagamento superior ao saldo da comanda.
- É possível realizar vários pagamentos parciais.

⚠️ Exceções personalizadas

O projeto possui uma hierarquia de exceções baseada em LanchoneteError.
```
LanchoneteError
│
├── MesaOcupadaError
├── AtendimentoEncerradoError
├── AtendimentoNaoEncontradoError
├── ProdutoNaoEncontradoError
├── QuantidadeInvalidaError
├── PagamentoInvalidoError
└── AtendimentoNaoQuitadoError
```
As exceções são utilizadas para impedir operações que violem as regras de negócio do sistema.

🖥️ Interface

A interface textual foi organizada em menus e telas, seguindo a separação entre navegação e interação com as funcionalidades.

Menus:
```
MenuPrincipal
│
├── MenuMesas
├── MenuProdutos
└── MenuAtendimentos
```
Telas:

TelaMesas
TelaProdutos
TelaAtendimentos

📊 Diagrama Entidade-Relacionamento

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
        Mesa mesa
        list pedidos
        list pagamentos
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
        Produto produto
        int quantidade
        float valor
    }

    PAGAMENTO {
        float valor
    }
    
📚 Conceitos utilizados

O projeto demonstra a aplicação dos seguintes conceitos de Programação Orientada a Objetos:

Classes e objetos;
Encapsulamento;
Abstração;
Herança;
Polimorfismo;
Relacionamento entre objetos;
Exceções personalizadas;
Type Hints;
Docstrings;
Organização em módulos e pacotes;
Gerenciamento de dados em memória.

🚀 Execução
Para executar o sistema, utilize:
python main.py

🎯 Fluxo principal
Cadastrar mesas e produtos
          ↓
Abrir atendimento
          ↓
Registrar pedidos
          ↓
Consultar consumo
          ↓
Registrar pagamentos parciais
          ↓
Consultar total pago e saldo
          ↓
Registrar pagamentos restantes
          ↓
Encerrar atendimento
          ↓
Liberar mesa
          ↓
Consultar histórico

📁 Organização das responsabilidades
MODELOS
    ↓
Objetos e regras do domínio

APLICAÇÃO
    ↓
Coleções em memória e coordenação

INTERFACE
    ↓
Menus, telas e interação

EXCEÇÕES
    ↓
Regras que impedem operações inválidas
