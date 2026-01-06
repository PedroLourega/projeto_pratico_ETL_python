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
            f"Ei {nickname}, que da hora que está jogando o {jogo}.",
            f"O {jogo} é top demais! Entra aí no discord {nickname}, bora trocar uma ideia!",
        ]
    elif status == 'Ausente': # Ausente
        frases = [
            f"{nickname}, volta aqui!"
        ]
    else: # Offline
        frases = [
            f"Sdds de você no {jogo}, {nickname}...",
            f"Quando voltar, avisa a gente para jogar {jogo} junto se der!",
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