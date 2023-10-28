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
        
        if resultado:
            print("O teste de atuar_sobre_atual foi bem-sucedido!")

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
        
        if resultado:
            print("O teste de atuar_sobre_tempo foi bem-sucedido!")

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
        
        if resultado:
            print("O teste de atuar_sobre_climatica foi bem-sucedido!")

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
        
        if resultado:
            print("O teste de atuar_sobre_chover foi bem-sucedido!")

if __name__ == '__main__':
    unittest.main()
