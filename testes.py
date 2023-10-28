import unittest
from amigo import *
from atuadores import *
import speech_recognition as sr
from nltk import corpus

CHAMANDO_AMIGO = "audios/chamando_amigo.wav"
CHAMANDO_OUTRO_NOME = "audios/chamando_outro_nome.wav"
TEMPERATURA_ATUAL = "audios/temperatura_atual.wav"
PREVISAO_AMANHA = "audios/previsao_amanha.wav"
CONDICAO_CLIMATICA = "audios/condicao_climatica.wav"
PREVISAO_CHUVA = "audios/previsao_chuva.wav"

class TesteNomeDoAssistente(unittest.TestCase):
    def testar_01_reconhecer_nome(self):
        with open(ARQUIVO_DE_CONFIGURACAO, "r", encoding="utf-8") as arquivo:
            assistente = json.load(arquivo)

            nome_assistente = assistente["nome"]

            arquivo.close()
        
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
        
        r = sr.Recognizer()
        with sr.AudioFile(CHAMANDO_AMIGO) as source:
            audio = r.listen(source)
            transcricao = r.recognize_google(audio, language="pt-BR")
            
        

        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        resultado = self.assertEqual(tokens[0], nome_assistente)

    def testar_02_nao_reconhecer_nome(self):
        with open(ARQUIVO_DE_CONFIGURACAO, "r", encoding="utf-8") as arquivo:
            assistente = json.load(arquivo)

            nome_assistente = assistente["nome"]

            arquivo.close()
            
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
        
        r = sr.Recognizer()
        with sr.AudioFile(CHAMANDO_OUTRO_NOME) as source:
            audio = r.listen(source)
            transcricao = r.recognize_google(audio, language="pt-BR")

        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        self.assertNotEqual(tokens[0], nome_assistente)

class TestAtuadores(unittest.TestCase):
        
    def test_atuar_sobre_atual(self):
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
        
        r = sr.Recognizer()
        with sr.AudioFile(TEMPERATURA_ATUAL) as source:
            audio = r.listen(source)
            transcricao = r.recognize_google(audio, language="pt-BR")

        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        resultado = atuar_sobre_atual(tokens[1], tokens[2])
        self.assertTrue(isinstance(resultado, bool))

    def test_atuar_sobre_tempo(self):
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
        
        r = sr.Recognizer()
        with sr.AudioFile(PREVISAO_AMANHA) as source:
            audio = r.listen(source)
            transcricao = r.recognize_google(audio, language="pt-BR")

        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        resultado = atuar_sobre_tempo(tokens[1], tokens[2])
        self.assertTrue(isinstance(resultado, bool))

    def test_atuar_sobre_climatica(self):
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
        
        r = sr.Recognizer()
        with sr.AudioFile(CONDICAO_CLIMATICA) as source:
            audio = r.listen(source)
            transcricao = r.recognize_google(audio, language="pt-BR")

        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        resultado = atuar_sobre_climatica(tokens[1], tokens[2])
        self.assertTrue(isinstance(resultado, bool))

    def test_atuar_sobre_chover(self):
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
        ''
        r = sr.Recognizer()
        with sr.AudioFile(PREVISAO_CHUVA) as source:
            audio = r.listen(source)
            transcricao = r.recognize_google(audio, language="pt-BR")

        tokens = tokenizar(transcricao.lower())
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        resultado = atuar_sobre_chover(tokens[1], tokens[2])
        self.assertTrue(isinstance(resultado, bool))

if __name__ == '__main__':
    unittest.main()

