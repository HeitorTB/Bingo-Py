import random
niveis = {
    0: {"players": 2, "linhas": 2, "colunas": 3},
    1: {"players": 4, "linhas": 3, "colunas": 4},
}

def exibir_matriz(matriz):
    for linha in matriz:
        print('  '.join(str(num) for num in linha))

intervalos = ((1, 10), (11, 20), (21, 30), (31, 40))


def verificação_dezena(nivel, matriz, niveis):
    colunas = niveis[nivel]["colunas"]
    num_sorteado = random.randint(1, colunas * 10)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num_sorteado:
                matriz[i][j] = f'({matriz[i][j]})' 
    return matriz 
        
                    



def criar_cartekas(nivel):
    matriz = []
    usados = []
    for i in range(niveis[nivel]["linhas"]):
        linha = []
        for c in range(niveis[nivel]["colunas"]):
            intervalo = intervalos[c]
            num = random.randint(intervalo[0], intervalo[1])
            while num in usados:
                num = random.randint(intervalo[0], intervalo[1])
            usados.append(num)
            if num < 10:
                linha.append(str(num).zfill(2))
            else:
                linha.append(num)
        matriz.append(linha)  
    exibir_matriz(matriz) 

def jogo(nivel):
    config = niveis[nivel]
    for c in range(1, config["players"] + 1):
        print(f"Jogador {c}")
        criar_cartekas(nivel)
        verificação_dezena(nivel,matriz=exibir_matriz,niveis=len(exibir_matriz))
        


jogo(0)









