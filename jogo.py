import random
niveis = {
    0: {"players": 2, "linhas": 2, "colunas":3},
    1: {"players": 4, "linhas": 3, "colunas":4},
}

intervalos=((1,10),(11,20),(21,30),(31,40))

matriz=[]

def criar_cartekas(nivel):
    for i in range(niveis[nivel]["linhas"]):
        matriz.append([])
        for c in range(niveis[nivel["colunas"]]):
            while matriz[i] not in matriz:
                matriz[i].append([random.randint(intervalos[c])])
    return matriz
            

def jogo(nivel):
    config = niveis[nivel]
    Sorted=[]

    for c in range (1, config["players"]+1):
        print("jogador", c)
        print(criar_cartekas(nivel))
        


jogo(1)
        









