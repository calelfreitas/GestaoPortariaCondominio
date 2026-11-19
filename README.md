# Sistema de gestão de Portaria de Condomínio:

Aplicação web desenvolvida em **Python** e **Django** para otimizar o controle operacional de portarias residenciais e comerciais, centralizando o cadastro de moradores, registro de encomendas, fluxo de visitantes, gestão de colaboradores e livro de ocorrências.

## Funcionalidades:

* **Painel Operacional (Dashboard):** Visão rápida do total de moradores cadastrados, entregas pendentes, últimas entradas de visitantes, ocorrências recentes e quadro de avisos dinâmico entre turnos.
* **Gestão de Moradores:** Cadastro completo com validação de CPF único, telefone, bloco e apartamento.
* **Controle de Entregas:** Registro de recebimento de encomendas vinculadas ao morador e controle de retirada.
* **Controle de Acesso (Entradas):** Registro de visitantes e prestadores de serviço com identificação por RG/CIN e destino.
* **Colaboradores:** Cadastro de funcionários da portaria/condomínio por cargo e turno de trabalho.
* **Livro de Ocorrências:** Registro detalhado de eventos e ocorrências por funcionário responsável.
* **Recursos de Interface:** Máscaras automáticas de CPF, RG/CIN e telefone, validação visual de formulários, relógio em tempo real e pesquisa instantânea nas tabelas.

## Ferreamntas utilizadas:

* **Back-end:** Python 3, Django
* **Front-end:** HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5, Bootstrap Icons
* **Banco de Dados:** SQLite (ambiente de desenvolvimento)

## Como executar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio