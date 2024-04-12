import random

class Baralho():
    def __init__(self):
        self.baralho = None #Baralho completo - carta - valor
        self.cartas = None #Baralho embalharado - carta
        self.gerar_baralho()

    
    def gerar_baralho(self):
        #ordenados pela ordem de poder do jogo########
        naipes = ['trevo','coração','copa','ouro']
        manilhas = [4,7,1,7]
        cartas = [3,2,'a','j','q','k'] 
        ###############################################
        deck_baralho = {}

        nivel = len(manilhas) + len(cartas)
        for naipe, manilha in zip(naipes,manilhas):
            deck_baralho[(manilha,naipe)] = nivel
            nivel-=1

        for carta in cartas:
            for naipe in naipes:
                if (carta,naipe) not in deck_baralho.keys():
                    deck_baralho[(carta,naipe)] = nivel
            nivel-=1
        self.baralho = deck_baralho
        cartas = list(self.baralho.keys())
        random.shuffle(cartas)
        self.cartas = cartas
    
    def distribui_cartas(self,qtd_cartas):
        #Distribui uma mão de cartas e atualiza o 'monte' 
        cartas_selecionadas = self.cartas[0:qtd_cartas]
        self.cartas = self.cartas[qtd_cartas:]
        all_letters = True
        letras = 0
    
        while all_letters:
            for carta in cartas_selecionadas:
                insignia = carta[0]
                if type(insignia) != int:
                    letras+=1
            if letras == 3:
                all_letters = True
                letras = 0
                cartas_selecionadas = self.cartas[0:qtd_cartas]
                self.cartas = self.cartas[qtd_cartas:]

                qtd_cartas+=qtd_cartas
            else:
                all_letters = False
        
        return cartas_selecionadas
