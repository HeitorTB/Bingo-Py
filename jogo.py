import random
niveis = {
    0: {"players": 2, "linhas": 2, "colunas": 3},
    1: {"players": 4, "linhas": 3, "colunas": 4},
}

def exibir_matriz(matriz):
    for linha in matriz:
        print('  '.join(str(num) for num in linha))
        
intervalos = ((1, 10), (11, 20), (21, 30), (31, 40))
numeros_sorteados1=[]

def criar_cartekas(nivel):
    matriz=[]
    usados=[]
    for i in range(niveis[nivel]["linhas"]):
        linha = []
        for c in range(niveis[nivel]["colunas"]):
            intervalo = intervalos[c]
            num = random.randint(intervalo[0], intervalo[1])
            while num in usados:
                num = random.randint(intervalo[0], intervalo[1])
            usados.append(num)
            linha.append(num)
        matriz.append(linha)
    return exibir_matriz(matriz)

def jogo(nivel):
    config = niveis[nivel]
    for c in range(1, config["players"] + 1):
        print(f"Jogador {c}")
        print(criar_cartekas(nivel))

jogo(1)









