# Projeto ETL voltado para Games (Python + Pandas)

Projeto prático que eu construí para estudar o fluxo **ETL (Extract, Transform, Load)**. A ideia foi criar um script que simula mensagens automáticas para uma base de jogadores para uma espécie de "Discord", lendo dados de um arquivo, processando regras de negócio e gerando um resultado.

Além do processamento de dados, implementei um **menu interativo** no terminal para visualizar e consultar as informações geradas.

## O que o código faz
- **Extract:** Lê uma planilha CSV (`jogadores.csv`) com ID, Nickname, Status e Jogo Favorito.
- **Transform:** Analisa o status de cada jogador (Online, Ausente ou Offline) e escolhe uma mensagem personalizada aleatória usando a biblioteca `random`.
- **Load:** Exporta os dados processados para um novo arquivo CSV (`jogadores_com_mensagens.csv`).
- **Interface (CLI):** Exibe uma tabela formatada com todos os jogadores e permite pesquisar a mensagem gerada através do ID.

## Tecnologias
- Python
- Pandas (Leitura, filtragem e escrita de dados)
- CSV (Estrutura de dados)

## Autor <br>

**Pedro Henrique Lourega Rodrigues** <br>
Estudante de Análise e Desenvolvimento de Sistemas <br>
GitHub: [@PedroLourega](https://github.com/PedroLourega) <br>