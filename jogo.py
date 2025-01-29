import random
niveis = {
    0: {"players": 2, "linhas": 2, "colunas": 3},
    1: {"players": 4, "linhas": 3, "colunas": 4},
}

def exibir_matriz(matriz):
    for linha in matriz:
        print('  '.join(str(num) for num in linha))

intervalos = ((1, 10), (11, 20), (21, 30), (31, 40))
     
def criar_cartelas(nivel):
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
    return matriz

def sortear_numero(nivel):
    config = niveis[nivel]
    colunas= config["colunas"]*10
    numSorted= random.randint(1,colunas)
    print(numSorted)

def jogo(nivel):
    config = niveis[nivel]
    while True:
        for c in range(1, config["players"] + 1):
            print(f"Jogador(a) {c}")
            matriz = criar_cartelas(nivel)  
            exibir_matriz(matriz)
        sortear_numero(nivel)
        break

jogo(1)