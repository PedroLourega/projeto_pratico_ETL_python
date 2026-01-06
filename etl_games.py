# Import da biblioteca pandas e do pack random
import pandas as pd
import random

# Configuração dos arquivos
ARQUIVO_ENTRADA = 'jogadores.csv'
ARQUIVO_SAIDA = 'jogadores_com_mensagens.csv'

# EXTRACT
def carregar_dados():
    print('[1/3] Iniciando a leitura dos dados de jogadores...')
    try:
        # A biblioteca pandas transforma os dados do arquivo CSV para uma tabela(DF)
        df = pd.read_csv(ARQUIVO_ENTRADA)
        
        print(f"Dados carregados com sucesso!! {len(df)} jogadores encontrados.")
        return df
    except FileNotFoundError:
        print(f"Erro: O Arquivo não foi localizado.")
        return None
    
def gerar_mensagem(nickname, status, jogo):
    if status == 'Online': # Online
        frases = [
            f"Ei {nickname}, que da hora que você está jogando {jogo}!",
            f"O {jogo} é top demais! Aproveita a jogatina, {nickname}!",
            f"Hoje é dia de fazer história no {jogo}, hein {nickname}?",
            f"Modo foco ativado! Destrói tudo no {jogo}, {nickname}!",
            f"Aproveita que está ON e farma muito XP no {jogo}, {nickname}!"
        ]
    elif status == 'Ausente': # Ausente
        frases = [
            f"{nickname}, volta aqui! O {jogo} não se joga sozinho.",
            f"Foi buscar um café, {nickname}? O {jogo} te espera!",
            f"Recarregando as energias para voltar com tudo no {jogo}, {nickname}?",
            f"Cochilo tático? Não esquece de salvar o progresso no {jogo}, {nickname}!"
        ]
    else: # Offline
        frases = [
            f"Sdds de você no {jogo}, {nickname}...",
            f"Quando voltar, avisa a gente para jogar {jogo} junto se der!",
            f"Faz tempo que não vejo suas skills no {jogo}, {nickname}.",
            f"Tudo pronto para o seu retorno lendario ao {jogo}, {nickname}?",
            f"O servidor (ou o save) de {jogo} sente sua falta, {nickname}!"
        ]
    
    return random.choice(frases)

# TRANSFORM
def processar_dados(df):
    print("[2/3] Criando mensagem personalizada...")

    mensagem = [] 

    # Percorre linha por linha da tabela
    for index, linha in df.iterrows():
        nick = linha['nickname']
        stat = linha['status']
        game = linha['jogo_principal']

        # chama a func que cria a frase
        msg = gerar_mensagem(nick, stat, game)

        # adc na lista e mostra com print
        mensagem.append(msg) 
        print(f"Processando dados de --> {nick} (status: {stat})")
    
    
    df['mensagem_enviada'] = mensagem 
    return df


# LOAD
def salvar_dados(df):
    print("[3/3] Salvando arquivo final, \n Por favor aguarde...")
    # index=false: serve para nao salvar a numeracao das linhas no arquivo
    df.to_csv(ARQUIVO_SAIDA, index=False)
    print(f" Arquivo '{ARQUIVO_SAIDA}' salvo com sucesso!")

if __name__ == "__main__":
    tabela = carregar_dados()
    
    if tabela is not None:
        tabela_transformada = processar_dados(tabela)
        salvar_dados(tabela_transformada)