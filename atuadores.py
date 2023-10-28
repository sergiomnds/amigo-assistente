def atuar_sobre_atual(acao, objeto):
    executado = False
    
    if acao == "temperatura" and objeto == "atual":
        executado = True
        
        print("A temperatura atual é em torno de 30 graus")

    return executado

def atuar_sobre_tempo(acao, objeto):
    executado = False
    
    if acao == "previsão" and objeto == "tempo":
        executado = True
        
        print("A previsão do tempo para amanhã é de sol com poucas nuvens")

    return executado

def atuar_sobre_climatica(acao, objeto):
    executado = False
    
    if acao == "condição" and objeto == "climática":
        executado = True
        
        print("A temperatura está em torno de 25 graus, com céu nublado. A umidade relativa do ar está em 60%. Sem previsões de chuva nas próximas horas.")

    return executado

def atuar_sobre_chover(acao, objeto):
    executado = False
    
    if acao == "vai" and objeto == "chover":
        executado = True
        
        print("A previsão de chuva para hoje é baixa, com 10% de chance.")

    return executado