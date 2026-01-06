# Projeto ETL voltado para Games (Python + Pandas)

Projeto prático que eu construí para estudar o fluxo **ETL (Extract, Transform, Load)**. A ideia foi criar um script que simula uma rede social para uma base de jogadores, lendo dados de um arquivo, processando regras de negócio e gerando um resultado final, o projeto roda localmente.

## O que o código faz
- **Extract:** Lê uma planilha CSV (`jogadores.csv`) com ID, Nickname, Status e Jogo Favorito.
- **Transform:** Analisa o status de cada jogador (Online, Ausente ou Offline) e escolhe uma mensagem personalizada aleatória usando a biblioteca `random`.
- **Load:** Exporta os dados processados para um novo arquivo CSV (`jogadores_com_mensagens.csv`).

## Tecnologias
- Python
- Pandas (Leitura e escrita de dados)
- CSV (Estrutura de dados)

##  Autor <br>

**Pedro Henrique Lourega Rodrigues** <br>
Estudante de Análise e Desenvolvimento de Sistemas  <br>
GitHub: [@PedroLourega](https://github.com/PedroLourega) <br>
