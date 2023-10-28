import speech_recognition as sr
from nltk import word_tokenize, corpus
import json

from atuadores import *
IDIOMA_CORPUS = "portuguese"
IDIOMA_FALA = "pt-BR"

# PERGUNTAS:
# Qual a temperatura atual?
# Qual a previsão do tempo para amanhã?
# Qual a condição climática em Vitória da Conquista?
# Vai chover hoje?

ARQUIVO_DE_CONFIGURACAO = "config.json"

ATUADORES = [
    {
        "nome": "atual",
        "atuar": atuar_sobre_atual
    },
    {
        "nome": "tempo",
        "atuar": atuar_sobre_tempo
    },
    {
        "nome": "climática",
        "atuar": atuar_sobre_climatica
    },
    {
        "nome": "chover",
        "atuar": atuar_sobre_chover
    }
]

def iniciar():
    iniciado = False
    palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
    reconhecedor = sr.Recognizer()

    with open(ARQUIVO_DE_CONFIGURACAO, "r", encoding="utf-8") as arquivo:
        assistente = json.load(arquivo)

        nome_assistente = assistente["nome"]
        acoes = assistente["acoes"]

        arquivo.close()

    iniciado = True
    print('Olá, sou seu Amigo! Respondo perguntas sobre o tempo!')
    return iniciado, palavras_de_parada, reconhecedor, nome_assistente, acoes

def escutar_fala(reconhecedor):
    tem_fala = False
    
    while not tem_fala:
        with sr.Microphone() as fonte_de_audio:
            reconhecedor.adjust_for_ambient_noise(fonte_de_audio)

            print("O que quer saber ?")
            try:
                fala = reconhecedor.listen(fonte_de_audio, timeout=5)
                tem_fala = True
            except:
                print("Não entendi o que você disse (Aperte Ctrl + C para sair)")

    return tem_fala, fala

def transcrever_fala(fala, reconhecedor):
    tem_transcricao = False
    
    transcricao = reconhecedor.recognize_google(
        fala, language=IDIOMA_FALA)
    tem_transcricao = True

    return tem_transcricao, transcricao.lower()


def tokenizar(transcricao):
    tokens = word_tokenize(transcricao)

    return tokens

def eliminar_palavras_de_parada(tokens, palavras_de_parada):
    tokens_filtrados = []

    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados

def validar_comando(tokens, nome_do_assistente, acoes):
    valido, acao, objeto = False, None, None

    if len(tokens) >= 2:
        if nome_do_assistente == tokens[0]:
            acao = tokens[1]
            objeto = tokens[2]

            for acao_prevista in acoes:
                if acao == acao_prevista['nome']:
                    if objeto in acao_prevista['objetos']:
                        valido = True

                        break

    return valido, acao, objeto


def executar_comando(acao, objeto):
    for atuador in ATUADORES:
        atuou = atuador["atuar"](acao, objeto)

        if atuou:
            break

if __name__ == "__main__":
    iniciado, palavras_de_parada, reconhecedor, nome_assistente, acoes = iniciar()
    try:  
        if iniciado:
            while True:
                tem_fala, fala = escutar_fala(reconhecedor)
                if tem_fala:
                    tem_transcricao, transcricao = transcrever_fala(
                        fala, reconhecedor)
                    if tem_transcricao:
                        tokens = tokenizar(transcricao)
                        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)

                        valido, acao, objeto = validar_comando(tokens, nome_assistente, acoes)
                        if (valido):
                            executar_comando(acao, objeto)
                        else:
                            print(f"Comando invalido")
        else:
            print("Não foi possível iniciar o assistente")
    except KeyboardInterrupt:
        print("Até mais!")
        
